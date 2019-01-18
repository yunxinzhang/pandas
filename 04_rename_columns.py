# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:37:45 2019

@author: zyx
"""

import pandas as pd

ufo = pd.read_csv('ufo.csv')

ufo.columns
ufo.describe(include='object')

ufo.rename(columns={'Colors Reported':'Colors_Reported', 
                    'Shape Reported': 'Shape_Reported'}, inplace=True)

cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = cols