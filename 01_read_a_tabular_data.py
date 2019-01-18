# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:12:03 2019

@author: zyx
"""

import pandas as pd

data = pd.read_table('chipotle.tsv')

data.head(n=5)

#sep
data = pd.read_table('u.user', sep='|')

#header
data = pd.read_table('u.user', sep='|', header=None)

#names
names = ['id', 'age', 'gender', 'occupation', 'zip_code']
data = pd.read_table('u.user', sep='|', header=None, names=names)
