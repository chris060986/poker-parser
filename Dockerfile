FROM chris060986/python-poker:0.30.1
MAINTAINER christoph.birk@gmail.com

WORKDIR /tmp
COPY setup.py .
RUN python setup.py install

WORKDIR /app
COPY build/lib/ ./
RUN ls -la .

CMD [ "python", "./poker_parser/webserver.py" ]


#FROM chris060986/python-poker:0.30.1
#MAINTAINER christoph.birk@gmail.com
#
#WORKDIR /app
#
#COPY . .
#RUN python setup.py install
#
#
#EXPOSE 5000
#ENTRYPOINT ['python']
#CMD [ 'python', './poker_parser/webserver.py' ]