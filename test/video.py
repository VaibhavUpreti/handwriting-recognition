from ultralytics import YOLO
import cv2

path=r'C:\Users\Gautam\Desktop\anpr\project\Kavach\1.png'
img=cv2.imread(path)

model=YOLO("best7.pt")
results = model.predict(source=img, conf=0.3, iou=0.1)
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

boxes = results[0].boxes

for i in boxes:
    temp=i.xyxy
    cv2.rectangle(img, (int(temp[0][0]),int(temp[0][1])), (int(temp[0][2]),int(temp[0][3])), (0,255,0), thickness=1)
    cv2.putText(img, "A",(int(temp[0][0]),int(temp[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

cv2.imshow("img",img)

cv2.waitKey(0)