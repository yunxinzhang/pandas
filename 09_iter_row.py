# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:32:39 2019

@author: zyx
"""

import pandas as pd
ufo = pd.read_csv('ufo.csv')

for index, row in ufo.iterrows():
    print(index, row)
    break