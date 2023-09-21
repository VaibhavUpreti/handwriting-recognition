# Handwriting Recognition Web Application

This application is designed to recognize handwriting from images.

## Demo

Check out the working demo in action:

https://user-images.githubusercontent.com/85568177/243087716-e8f28b96-f58a-4b33-b90e-76d843d0ec35.mp4

## Installation

Choose one of the following methods to install the application:

1. Manual Setup
2. Docker
3. Helm Chart (Kubernetes)

### Manual Setup

If you prefer to set up the application manually

#### Requirements

Make sure you have the following prerequisites installed:

1. Python version >= 3.8
2. Required Python packages can be found in [requirements.txt](https://github.com/VaibhavUpreti/handwriting-recognition/blob/master/src/requirements.txt).
3. CtCWordBeamSearch
4. SimpleHTR (optional)

#### Steps

Recommended to use pyenv 3.10

```python
pip install -r src/requirements.txt
```

This will install the following packages
- opencv-python
- editdistance
- ultralytics
- flask
- tensorflow
- lmdb
- path
- gunicorn

```python
git clone https://github.com/githubharald/CtCWordBeamSearch
cd CtCWordBeamSearch
pip install .
```

Start Server

```bash
python3 src/app.py
```

Navigate to http://localhost:3000

### Docker

Supported Docker images for your convenience:

1. [linux/amd64](https://github.com/VaibhavUpreti/handwriting-recognition/pkgs/container/handwriting-recognition) - Built using GitHub Actions Runner. See the [workflow file](https://github.com/VaibhavUpreti/handwriting-recognition/blob/master/.github/workflows/docker-publish.yml) for details.
2. [linux/arm64](https://hub.docker.com/r/vaibhavupreti/handwriting-recognition) - Available on Docker Hub.

```bash
docker pull ghcr.io/vaibhavupreti/handwriting-recognition:latest
docker run -p 3000:3000 <image_id>
```
### Helm Chart (Kubernetes)

Using Helm...

```bash
helm install handy helmchart
```

## Tech Stack

1. Flask
2. AWS EC2
3. Caddy web server
