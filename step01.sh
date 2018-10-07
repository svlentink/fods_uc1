#!/bin/sh

DATADIR=/tmp/dataset

mkdir -p $DATADIR
cd $DATADIR

if ! [ -f $DATADIR/*.jsons ]; then
  read -p "Please specify the path to the dataset (e.g. /home/slentink/geo*.tgz):" TARPATH
  tar xfz $TARPATH
  mv $DATADIR/*.jsons totalset.jsons
fi

head -10 totalset.jsons > first10.jsons
#head -1000 totalset.jsons > first1k.jsons
split -l 1000 --numeric-suffixes totalset.jsons splitset
ls -alh
wc -l *
