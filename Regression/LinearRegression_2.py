# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 17:22:26 2020

@author: HP
"""


import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\lrm.xlsx")
model = LinearRegression()
model.fit(data['Student_Population'].values.reshape(-1,1),data['Sales'].values.reshape(-1,1))
print(model.intercept_[0])
print(model.coef_[0][0])
print(model.predict([[10]]))
""" 60+5x=y"""
