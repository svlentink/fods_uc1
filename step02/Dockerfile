FROM continuumio/anaconda3
RUN pip install pymongo #distributed 1.21.8 requires msgpack, which is not installed.
COPY main.py /
VOLUME /datadir
ENTRYPOINT ["/main.py"]
