FROM chris060986/python-poker:0.30.1
MAINTAINER christoph.birk@gmail.com

WORKDIR /app

COPY poker_parser /app/poker_parser
COPY setup.py /app
RUN python setup.py install

CMD [ "python", "./poker_parser/webserver.py" ]
