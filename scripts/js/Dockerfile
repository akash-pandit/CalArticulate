# Dockerfile for javascript files
FROM node:20.11.1-slim

# set up working tree for js scripts & tests to match project tree
RUN mkdir -p scripts/js
RUN mkdir -p test/js
RUN apt update && apt install tree
COPY package* package* 
COPY . ./scripts/js
COPY ../../tests/js ./test/js

# RUN npm install 

# CMD ["node", "./scripts/js/scrapeURLsMain.js"]