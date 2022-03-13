# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:20:37 2022

@author: 18053
"""


import os
import pandas as pd
import numpy as np

df = pd.read_csv('data.tsv', sep='\t', header=None)
df.columns = ['word', 'relation', 'related_word']
df = df[df['relation'] == "rel:etymology"]

df['word'] = df['word'].apply(lambda x: x.split(': '))
df['related_word'] = df['related_word'].apply(lambda x: x.split(': '))

df['word_language'] = df['word'].apply(lambda x: x[0])
df['word'] = df['word'].apply(lambda x: x[1])

df['related_word_language'] = df['related_word'].apply(lambda x: x[0])
df['related_word'] = df['related_word'].apply(lambda x: x[1])

df = df[['word', 'word_language', 'related_word',
         'related_word_language']]

# df = df[df['word_language'] == 'eng']

lang_list = df['related_word_language'].unique()
lang_list.sort()
# print(lang_list)

df = df[~df['word'].str.contains('-')]

x = df[(df['word_language'] == 'eng')]
pivot = pd.pivot_table(data = x, index = 'related_word_language',
                       values='word_language',
                       aggfunc='count').sort_values('word_language', ascending=False)
# enm = middle english
# ang = old english
print(pivot.head(15))