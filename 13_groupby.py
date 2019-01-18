# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 17:43:22 2019

@author: zyx
"""

import pandas as pd

drink = pd.read_csv('drinks.csv')

drink.dtypes

drink.beer_servings.mean()

drink.groupby('continent').beer_servings.mean()

drink.groupby('continent').beer_servings.agg(['min','max','mean','count'])

import matplotlib.pyplot as plt

drink.groupby('continent').mean().plot(kind='bar')