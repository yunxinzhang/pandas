# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:22:32 2019

@author: zyx
"""

import pandas as pd

data = pd.read_table('ufo.csv', sep=',')

type(data['City'])

data['City'] +  data['State']

#Adding a new column
data['Location'] = data['City'] + ',' + data['State']