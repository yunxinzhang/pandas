# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:52:52 2019

@author: zyx
"""

import pandas as pd

movies = pd.read_csv('imdb_1000.csv')

movies.title.sort_values(ascending=False)

type(movies.title.sort_values())

movies.sort_values('title')

type(movies.sort_values('title'))
kk = movies.sort_values(['content_rating','duration'])