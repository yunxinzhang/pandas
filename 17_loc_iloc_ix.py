# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 02:25:01 2019

@author: zyx
"""

import pandas as pd

ufo = pd.read_csv('ufo.csv')

# Easy to use
x1 = ufo.iloc[0:2,0:2] #()

# Can not use number 
x2 = ufo.loc[0:2,'City':'State'] #[]

x3 = ufo.ix[0:2, 0:2] #[)