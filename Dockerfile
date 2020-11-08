FROM chris060986/python-poker:0.30.1
MAINTAINER christoph.birk@gmail.com

WORKDIR /tmp
COPY setup.py .
RUN python setup.py install

WORKDIR /app
COPY /src ./

CMD [ "python", "./webserver.py" ]