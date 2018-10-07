#!/usr/bin/env python3

inp='/datadir/first1k.jsons'
#inp='/datdair/split*'
cols2keep= [
'timestamp_ms', #instead of created_at
'id_str', #instead of id, to avoid math on it
'text'
]


import numpy as np
import pandas as pd
from pymongo import MongoClient
from pprint import pprint
from glob import glob
from time import sleep
import json

#sleep(10) #wait for mongodb
dbc = MongoClient('db', 27017)

def remove_columns(df,cols_to_keep,cols_to_remove=[]):
  if len(cols_to_remove) == 0:
    for c in df.columns:
      if c not in cols_to_keep:
        cols_to_remove.append(c)
  print('Removing',cols_to_remove)
  return df.drop(columns=cols_to_remove)

def df2mongo(df,dbc,dbname='dataset',tablename='table1'):
  db = dbc[dbname]
#  db.authenticate('root', 'onlylocalxs')
  tbl = db[tablename]
  ts = len(df)
  if ts <= 1000:
    arr = json.loads(df.T.to_json()).values()
    tbl.insert_many(arr)
    return tbl
  i=0
  for r in df.iterrows():
    tbl.insert_one(r)
    i+=1
    if i %100 == 0:
      print('Inserting into Mongo',dbname,i,ts)
  return tbl

def parse_inp(inp):
  fls = glob(inp)
  i=0
  tf=len(fls)
  for f in fls:
    df = pd.read_json(f, orient='columns', lines=True)
    cleandf = remove_columns(df,cols2keep)
    df2mongo(cleandf,dbc)
    i+=1
    print('Parsing',i,tf)


parse_inp(inp)
