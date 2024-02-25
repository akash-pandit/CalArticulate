#!/usr/bin/bash

docker rmi test -f
docker build -t test .
docker run test