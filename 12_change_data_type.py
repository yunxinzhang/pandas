# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:36:37 2019

@author: zyx
"""

import pandas as pd

drink = pd.read_csv('drinks.csv')

drink.dtypes

drink.beer_servings = drink.beer_servings.astype(float)

chips = pd.read_table('chipotle.tsv')

chips.dtypes

chips.item_price.str.replace('$','').astype(float).mean()