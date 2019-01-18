# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:05:38 2019

@author: zyx
"""

import pandas as pd

data = pd.read_table('chipotle.tsv')

data.item_name.str.upper()

data.item_name.str.contains('Chicken')

data.choice_description.str.replace('[','').str.replace(']', '')

data.choice_description.str.replace('[\[\]]', '')