FROM continuumio/anaconda3
RUN pip install pymongo #distributed 1.21.8 requires msgpack, which is not installed.

#https://github.com/conda-forge/pygridgen-feedstock/issues/10
RUN apt update; apt install -y libgl1-mesa-glx

COPY main.py /
VOLUME /datadir
ENTRYPOINT ["/main.py"]
