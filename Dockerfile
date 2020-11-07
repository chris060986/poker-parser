FROM chris060986/python-poker:0.30.1
MAINTAINER christoph.birk@gmail.com

WORKDIR /app

COPY poker_parser /app
COPY setup.py /app
RUN python setup.py install

CMD [ "python", "./webserver.py" ]
