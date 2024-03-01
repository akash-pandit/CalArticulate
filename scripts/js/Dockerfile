# Dockerfile for javascript files
FROM node:20.11.1-slim

# set up working tree for js scripts & tests to match project tree
COPY . .

RUN npm install 

CMD ["node", "scrapeURLsMain.js"]