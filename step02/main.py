#!/usr/bin/env python3

inpf='/datadir/first10.jsons'
cols2keep= [
'timestamp_ms', #instead of created_at
'id_str', #instead of id, to avoid math on it
'text'
]


import numpy as np
import pandas as pd

#with open(inpf, 'r') as
df = pd.read_json(inpf, orient='columns', lines=True)

def remove_columns(df,cols_to_keep,cols_to_remove=[]):
  if len(cols_to_remove) == 0:
    for c in df.columns:
      if c not in cols_to_keep:
        cols_to_remove.append(c)
  print('Removing',cols_to_remove)
  return df.drop(columns=cols_to_remove)

  
df2 = remove_columns(df,cols2keep)

