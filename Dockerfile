FROM chris060986/python-poker:0.30.1
MAINTAINER christoph.birk@gmail.com

WORKDIR /

COPY poker_parser/ /app/
COPY setup.py /setup.py
RUN python setup.py install

#RUN ls -la /app

EXPOSE 5000

ENTRYPOINT [ 'python3' ]

CMD [ '/app/webserver.py' ]
