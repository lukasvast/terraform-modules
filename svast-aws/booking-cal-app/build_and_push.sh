#!/bin/bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 199000118951.dkr.ecr.us-east-1.amazonaws.com
docker buildx build --platform linux/amd64 -t booking-cal-ecr .
docker tag booking-cal-ecr:latest 199000118951.dkr.ecr.us-east-1.amazonaws.com/booking-cal-ecr:0.0.5
docker push 199000118951.dkr.ecr.us-east-1.amazonaws.com/booking-cal-ecr:0.0.5

# LOCAL RUN ON http://127.0.0.1:8080/
# pip3 install requirements.txt
# python3 app.py

