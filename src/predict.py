from ultralytics import YOLO
from cv2 import rectangle, putText, FONT_HERSHEY_SIMPLEX, COLOR_BGR2GRAY , cvtColor
from model import Model, DecoderType
from typing import List
from dataloader_iam import Batch
from preprocessor import Preprocessor

class FilePaths:
    """Filenames and paths to data."""
    fn_char_list = '../model/charList.txt'
    fn_summary = '../model/summary.json'
    fn_corpus = '../data/corpus.txt'


def char_list_from_file() -> List[str]:
    with open(FilePaths.fn_char_list) as f:
        return list(f.read())

def get_img_height() -> int:
    """Fixed height for NN."""
    return 32

def infer(img , model: Model) -> str:
    """Recognizes text in image provided by img."""

    img=cvtColor(img, COLOR_BGR2GRAY)
    
    preprocessor = Preprocessor((128,32), dynamic_width=True, padding=16)
    img = preprocessor.process_img(img)

    batch = Batch([img], None, 1)
    recognized = model.infer_batch(batch, True)
    # print(f'Recognized: "{recognized[0]}"')
    # print(f'Probability: {probability[0]}')
    return recognized[0][0]



def img_to_text(img,model):
    """image to text"""

    text = infer(img , model)
    return text

def word_pred(img,cord,ctc_beam):
    model=YOLO("word.pt")
    results = model.predict(source=img[cord[1]:cord[3],cord[0]:cord[2]], conf=0.3, iou=0.1)
    boxes = results[0].boxes
    word=[]
    for i in boxes:
        temp=i.xyxy
        # print(temp)
        word.append([int(temp[0][0])+cord[0],int(temp[0][1])+cord[1], int(temp[0][2])+cord[0],int(temp[0][3])+cord[1]])
        # Buggy
        # word.append([int(temp[0][0])+cord[0]-10,int(temp[0][1])+cord[1]-10, int(temp[0][2])+cord[0]+10,int(temp[0][3])+cord[1]+10])
    
    word = sorted(word, key=lambda x:x[0])

    for i in word:
        i.append(img_to_text(img[i[1]:i[3],i[0]:i[2]],ctc_beam))

    return word

def line_pred(img,dim,ctc_beam):
    word=[]
    model=YOLO("line.pt")
    results = model.predict(source=img, conf=0.3, iou=0.7)
    boxes = results[0].boxes
    line=[]
    for i in boxes:
        temp=i.xyxy
        line.append([int(temp[0][0]),int(temp[0][1]), int(temp[0][2]),int(temp[0][3])])
    
    line = sorted(line, key=lambda x:x[1])

    for i in line:
        word.extend(word_pred(img,[i[0],i[1],i[2],i[3]],ctc_beam))

    return word

def img_text(word):
    text=""
    for i in word:
        text=text+" "+i[4]
    
    return text

def draw_img(img,word):
    for i in word:
        img=rectangle(img, (i[0],i[1]), (i[2],i[3]), (0,0,0), thickness=2)
        img=putText(img, i[4],(i[0],i[1]), FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 2)

    return img

def get_img_text(img):
    model = Model(char_list_from_file(), DecoderType.WordBeamSearch , must_restore=False, dump=False)
    shape_img=img.shape
    dim=shape_img[0:2]
    boxes = line_pred(img,dim,model)
    img=draw_img(img,boxes)
    print(boxes)
    text=img_text(boxes)
    return (img,text)
