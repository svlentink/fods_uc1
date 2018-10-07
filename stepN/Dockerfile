FROM continuumio/anaconda3

#https://github.com/conda-forge/pygridgen-feedstock/issues/10
RUN pip install pymongo descartes shapely gensim msgpack; \
  apt update; \
  apt install -y libgl1-mesa-glx

VOLUME /datadir
ENTRYPOINT ["/main.py"] # mounted via docker-compose
