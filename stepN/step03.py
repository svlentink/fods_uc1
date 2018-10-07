#!/usr/bin/env python3

import re
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

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string
import nltk

import gensim
from gensim import corpora


from pymongo import MongoClient
dbc = MongoClient('db', 27017)

def get_df_from_mongo(dbc,dbname='dataset',tablename='table1'):
  collection=dbc[dbname][tablename]
  data = collection.find()
  df =  pd.DataFrame(list(data))
  return df

df = get_df_from_mongo(dbc)

# https://alysivji.github.io/importing-mongo-documents-into-pandas-dataframes.html#Explore-and-Analyze-Data
def gen_figs(df, size=7, outputdir='/datadir',kinds=['bar','line','hist','area']):
  for col in df.columns:
    series = df[col]
    data = pd.value_counts(series.values)#, sort=False)
    t = 'Top ' + str(size) + ' ' + col
    for k in kinds:
      #ax = plt.subplots()
      outf = outputdir + '/' + col +'-' + k + '.png'
      p = data[:size].plot(kind=k,color='black',title=t)#,ax=ax)
      f = p.figure
      f.savefig(outf)#https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.savefig
      plt.gcf().clear()
      print('Saved',outf)


gen_figs(df)

# Topic analysis – Unsupervised learning
# Specifically: using Latent Dirichlet Allocation with nltk and gensim

nltk.download('stopwords')
# Create a set of stopwords
stop = set(stopwords.words('english'))

# Create a set of punctuation words 
exclude = set(string.punctuation) 

nltk.download('wordnet')
# This is the function makeing the lemmatization
lemma = WordNetLemmatizer()

# In this function we perform the entire cleaning
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


df['text'] = df['text'].apply(lambda s: re.sub(r'http.*?\ ','',s)  )
# This is the clean corpus.
txts = df['text'].values
doc_clean = [clean(doc).split() for doc in txts]



# Creating the term dictionary of our courpus, where every unique term is assigned an index
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=2, id2word = dictionary, passes=100)

# Print 2 topics and describe then with 4 words.
topics = ldamodel.print_topics(num_topics=2, num_words=4)

i=0
for topic in topics:
    print ("Topic",i ,"->", topic)     
    i+=1

