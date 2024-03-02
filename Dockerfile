FROM python:3.10-slim as python-env
FROM node:20.11.1-slim as node-env

WORKDIR /db-setup/
COPY ./scripts/python ./scripts/python
COPY ./scripts/js/package* .
COPY ./scripts/js/scrape* ./scripts/js
COPY ./scripts/js/node_modules ./node_modules/
COPY ./data/* ./data/

RUN pip install requests

RUN python3 gen_institutions.py
RUN python3 gen_urls.py

# ====================================
#  TBD: Finish multi-stage dockerfile
# ====================================

# Stage 2
FROM node:20.11.1-slim

# set up working tree for js scripts & tests to match project tree
WORKDIR /js_scripts
COPY ./scripts/js/package* .
COPY ./scripts/js/scrape* /js_scripts/
COPY ./scripts/js/node_modules /node_modules/
COPY ./data/* /data/

RUN apt-get update && apt-get install -y libgtk-3-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2
RUN npm install 

# CMD ["node", "scrapeURLsMain.js"]
CMD ["ls", "../data"]
