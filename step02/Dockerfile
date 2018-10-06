#FROM python:alpine
#RUN apk add --no-cache alpine-sdk #gcc needed during pip install
#COPY requirements.txt /
#RUN pip install -r /requirements.txt
FROM continuumio/anaconda3
COPY main.py /
VOLUME /datadir
ENTRYPOINT ["/main.py"]
