#!/usr/bin/env python3

inp='/datadir/first10.jsons'
inp='/datdair/split*'
cols2keep= [
'timestamp_ms', #instead of created_at
'id_str', #instead of id, to avoid math on it
'text',
'lang',
'place.country_code',
'user.followers_count'
] # the id string is needed to make them unique


import numpy as np
import pandas as pd
from pymongo import MongoClient
from pprint import pprint
from glob import glob
from time import sleep
import json
from pandas.io.json import json_normalize

sleep(10) #wait for mongodb
dbc = MongoClient('db', 27017)

def remove_columns(df,cols_to_keep,cols_to_remove=[]):
  if len(cols_to_remove) == 0:
    for c in df.columns:
      if c not in cols_to_keep:
        cols_to_remove.append(c)
  print('Removing',cols_to_remove)
  df.drop(columns=cols_to_remove,errors='ignore',inplace=True,axis=1)

def remove_dots_from_cols(df):
  for n in df.columns:
    if '.' in n:
      df.rename(columns={n: n[n.rfind('.')+1:]}, inplace=True)

def df2mongo(df,dbc,dbname='dataset',tablename='table1'):
  db = dbc[dbname]
#  db.authenticate('root', 'onlylocalxs')
  tbl = db[tablename]
  remove_dots_from_cols(df)
  ts = len(df)
  if ts <= 1000:
    tmp = df.to_json(orient='records')
    arr = json.loads(tmp)#.values()
    tbl.insert_many(arr)
    return tbl
  i=0
  for r in df.iterrows():
    tbl.insert_one(r)
    i+=1
    if i %100 == 0:
      print('Inserting into Mongo',dbname,i,ts)
  return tbl

#https://github.com/pandas-dev/pandas/pull/21164
#https://stackoverflow.com/questions/21411992/is-there-a-way-to-config-python-json-library-to-ignore-fields-that-has-null-valu
# got an error on: "utc_offset": -25200,
def remove_nulls(d):
  return {k: v for k, v in d.items() if v is not None}

def parse_inp(inp):
  fls = glob(inp)
  i=0
  tf=len(fls)
  for f in fls:
    #df = pd.read_json(f, orient='columns', lines=True)
    #BEGIN instead of read_json
    # looking back, we could have solved it using .apply or .applymap
    dfs = []
    with open(f) as fl:
      for l in fl.readlines():
        a = json.loads(l,object_hook=remove_nulls)
        b = json_normalize(a,errors='ignore')
        dfs.append(b)
    df = pd.concat(dfs)
    #END instead of read_json
    remove_columns(df,cols2keep)#does inplace
    df.set_index('id_str',inplace=True)
    df2mongo(df,dbc)
    i+=1
    print('Parsing file',i,tf)


parse_inp(inp)
