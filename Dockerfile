FROM python:3.10-slim

RUN mkdir -p /app/
RUN mkdir -p /data/
WORKDIR /app/
RUN pip install requests
RUN pip install selenium
COPY . .
COPY ../data/ ../data/
EXPOSE 3000

CMD [ "python3", "./app/getURLs.py" ]