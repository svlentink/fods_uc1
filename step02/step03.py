#!/usr/bin/env python3

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg') #since we run dockerized
import matplotlib.cm as cm
from matplotlib.colors import rgb2hex
#from descartes import PolygonPatch
#from shapely.geometry import Polygon, MultiPolygon

from pymongo import MongoClient
dbc = MongoClient('db', 27017)

def get_df_from_mongo(dbc,dbname='dataset',tablename='table1'):
  collection=dbc[dbname][tablename]
  data = collection.find()
  df =  pd.DataFrame(list(data))
  return df

# https://alysivji.github.io/importing-mongo-documents-into-pandas-dataframes.html#Explore-and-Analyze-Data
def gen_figs(df, size=7, outputdir='/datadir'):
  for col in df.columns:
    series = df[col]
    data = pd.value_counts(series.values)#, sort=False)
    #ax = plt.subplots()
    outf = outputdir + '/' + col + '.png'
    t = 'Top ' + str(size) + ' ' + col
    p = data[:size].plot(kind='bar',color='black',title=t)#,ax=ax)
    f = p.figure
    f.savefig(outf)#https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.savefig
    plt.gcf().clear()
    print('Saved',outf)

df = get_df_from_mongo(dbc)
gen_figs(df)

