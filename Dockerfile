FROM chris060986/python-poker:latest
MAINTAINER christoph.birk@gmail.com

WORKDIR /app

COPY parser/*.py .
