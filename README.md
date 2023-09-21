# Handwriting Recognition Web Application

This application is designed to recognize handwriting from images.

## Requirements

Make sure you have the following prerequisites installed:

1. Python version >= 3.8
2. Required Python packages can be found in [requirements.txt](https://github.com/VaibhavUpreti/handwriting-recognition/blob/master/src/requirements.txt).
3. CtCWordBeamSearch
4. SimpleHTR (optional)

## Demo

Check out the working demo in action:

![Handwriting Recognition Demo](https://user-images.githubusercontent.com/85568177/243087716-e8f28b96-f58a-4b33-b90e-76d843d0ec35.mp4)

## Docker Images

Supported Docker images for your convenience:

1. [linux/amd64](https://github.com/VaibhavUpreti/handwriting-recognition/pkgs/container/handwriting-recognition) - Built using GitHub Actions Runner. See the [workflow file](https://github.com/VaibhavUpreti/handwriting-recognition/blob/master/.github/workflows/docker-publish.yml) for details.
2. [linux/arm64](https://hub.docker.com/r/vaibhavupreti/handwriting-recognition) - Available on Docker Hub.

## Tech Stack

1. Flask
2. AWS EC2
3. Caddy web server
