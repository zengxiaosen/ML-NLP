from nltk.book import *
import pandas as pd
from pandas import DataFrame
import nltk
d = ['pets insurance','pets insure','pet insurance','pet insur','pet insurance"','pet insu']
df = DataFrame(d)
# print df
df.columns = ['Words']
# print df
tokenizer = nltk.RegexpTokenizer(r'w+')
# tokenizer = nltk.RegexpTokenizer
df["Stemming Words"] = ""
df["Count"] = 1
j = 0
while (j <= 5):
  for word in tokenizer.tokenize(df["Words"][j]):
    df["Stemming Words"][j] = df["Stemming Words"][j] + " " + nltk.PorterStemmer().stem_word(word)
  j += 1
print df

# uniqueWords = df.groupby(['Stemming Words'], as_index=False).sum().sort(['Count'])
# print uniqueWords




