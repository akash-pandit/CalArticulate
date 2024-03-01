# Dockerfile for javascript files
FROM node:20.11.1-slim

# set up working tree for js scripts & tests to match project tree
WORKDIR /js_scripts
COPY ./scripts/js/package* .
COPY ./scripts/js/scrape* /js_scripts/
COPY ./scripts/js/node_modules /node_modules/
COPY ./data/* /data/

RUN apt-get update && apt-get install -y libgtk-3-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2
RUN npm install 
EXPOSE 4000

CMD ["node", "scrapeURLsMain.js"]

# IT WORKS!!! HALLELUJAH!!!