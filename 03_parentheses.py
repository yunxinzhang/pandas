# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:28:58 2019

@author: zyx
"""

import pandas as pd

data = pd.read_csv('imdb_1000.csv')

data.describe()

data.shape

data.dtypes

type(data)

