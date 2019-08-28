#!/bin/bash
docker-compose up -d analysis
docker exec -it analysis /bin/bash
