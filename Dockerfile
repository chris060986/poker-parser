FROM chris060986/python-poker:0.30.1
MAINTAINER christoph.birk@gmail.com

WORKDIR /tmp

COPY dist/pokerstars_parser*.egg /tmp/pokerstars_parser.egg

RUN pip install /tmp/pokerstars_parser.egg

WORKDIR /app

CMD [ "python", "./parseme.py" ]
