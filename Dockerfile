FROM chris060986/python-poker:0.30.3
MAINTAINER christoph.birk@gmail.com

WORKDIR /tmp
COPY setup.py .
RUN python setup.py install

WORKDIR /app
COPY /src ./

ENV DATABASE_URL="my-poker-couch" \
    DATABASE_PORT=5984

CMD [ "python", "./webserver.py" ]