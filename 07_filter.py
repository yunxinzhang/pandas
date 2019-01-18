# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:05:52 2019

@author: zyx
"""
import pandas as pd

movies = pd.read_csv('imdb_1000.csv')

type(movies.duration > 200)

long_movie = movies[movies.duration > 200]

long_movie.title