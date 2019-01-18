# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:04:18 2019

@author: zyx
"""

import pandas as pd

movies = pd.read_csv('imdb_1000.csv')

movies.genre.describe()

movies.genre.value_counts()

movies.genre.value_counts(normalize=True)

movies.genre.unique()

movies.genre.nunique()

movies.duration.describe()

movies.duration.value_counts()

movies.duration.plot(kind='hist')

movies.genre.value_counts().plot(kind='bar')