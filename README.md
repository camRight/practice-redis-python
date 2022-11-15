# Redis/Docker Compose
---

### Introduction
The Thermostat Company has a web server and a redis database to deploy on their server, but need some help with container orchestration.  

Requirements
---
 1. Set up two Docker containers: one for server.py and one for redis
 2. Define a `docker-compose.yml` with the following setup:

     2a. the redis container should have some persistence features. \
         if a new redis image gets run, the newer container should be able to access the old cache. 

     2b. Do not expose redis ports outside of localhost 

     2c. server.py should be able to connect to the redis server

Questions
---
 1. What should happen when one of the containers exit?
 2. How would you get the redis container to update when a new stable release comes out?
 3. How would you set up docker-compose.yml to run on startup?
