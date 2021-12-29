#!/bin/bash

IMAGE_NAME="personal-api"
TAG="0.1.0"

docker build -t $IMAGE_NAME:$TAG .

echo "[i] Done."