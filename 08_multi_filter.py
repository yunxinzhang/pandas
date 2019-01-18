# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:16:07 2019

@author: zyx
"""
import pandas as pd

movies = pd.read_csv('imdb_1000.csv')

long_Drama = movies[(movies.duration > 200) & (movies.genre =='Drama')]

var_movies = movies[movies.genre.isin(['Crime', 'Action'])]
