# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:44:21 2019

@author: zyx
"""
import pandas as pd

dk = pd.read_csv('drinks.csv')

dk.head(n=5)
dk.drop('continent', axis=1).columns

dk.mean(axis=0)

dk.mean(axis=1)