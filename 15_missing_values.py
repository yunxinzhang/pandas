# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:30:37 2019

@author: zyx
"""


import pandas as pd

ufo = pd.read_csv('ufo.csv')

ufo.isnull().tail()

ufo.isnull().sum()

ufo[ufo.City.isnull()]

ufo.dropna(how='any').shape
ufo.dropna(how='all').shape

ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape

ufo['Shape Reported'].value_counts()

ufo['Shape Reported'].value_counts(dropna=False)

ufo['Shape Reported'].fillna(value='xxx', inplace=True)