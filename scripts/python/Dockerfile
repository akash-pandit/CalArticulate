# Dockerfile for python scripts
FROM python:3.10-slim

RUN pip install requests
COPY . .
COPY ../data/get_* .
COPY 

CMD [ "python3", "./app/getURLs.py" ]