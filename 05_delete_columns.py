# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:48:08 2019

@author: zyx
"""

import pandas as pd
import numpy as np

ufo = pd.read_csv('ufo.csv')

ufo.shape

ufo.drop('Colors Reported', axis=1, inplace=True)

ufo.columns

ufo.drop(['State','City'], axis=1, inplace=True)

# drop  object
movies = pd.read_csv('imdb_1000.csv')
movies.dtypes
kk = movies.select_dtypes(include=[np.number])