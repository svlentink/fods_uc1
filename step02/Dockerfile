FROM continuumio/anaconda3
RUN pip install pymongo
COPY main.py /
VOLUME /datadir
ENTRYPOINT ["/main.py"]
