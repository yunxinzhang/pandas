# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 02:57:19 2019

@author: zyx
"""

from sklearn import datasets
df = datasets.load_iris()

x = df.data
y = df.target



from sklearn.model_selection import train_test_split

xtr, xt, ytr, yt = train_test_split(x,y)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=30)
rfc.fit(xtr, ytr)

s = rfc.score(xt, yt)

yp = rfc.predict(xt)
import numpy as np
idx = np.arange(len(yp))
import pandas as pd
pd.DataFrame({'id':idx, 'predict':yp}).set_index('id').to_csv('res.csv')

