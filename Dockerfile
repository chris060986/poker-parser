FROM chris060986/python-poker:0.30.1
MAINTAINER christoph.birk@gmail.com

WORKDIR /app

COPY parser/*.py ./

CMD [ "python", "./parseme.py" ]
