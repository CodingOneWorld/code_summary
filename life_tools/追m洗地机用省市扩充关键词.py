"""
用省市扩充已有关键词
"""

import pandas as pd

df=pd.read_csv('追m关键词扩充v1.csv')
print(df.head())

words=df['key_word'].values

new_words=[]
for w in words:
    w1=w.replace('追觅','添可')
    print(w1)
    new_words.append(w1)




