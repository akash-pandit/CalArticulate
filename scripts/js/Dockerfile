# Dockerfile for javascript files
FROM node:20.11.1-slim

# set up working tree for js scripts & tests to match project tree
RUN mkdir -p scripts/javascript
RUN mkdir tests/javascript
COPY . ./scripts/javascript
COPY ../../tests/javascript ./tests/javascript

RUN npm install 

