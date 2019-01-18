# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:41:50 2019

@author: zyx
"""

import pandas as pd

drink = pd.read_csv('drinks.csv')

drink.index

drink.columns

drink[drink.continent=='South America']

drink.loc[23, 'country']

drink.set_index('country', inplace=True)

drink.index

drink.shape

drink.loc['Brazil', 'beer_servings']

drink.reset_index(inplace=True)

drink.describe().loc['25%', 'beer_servings']