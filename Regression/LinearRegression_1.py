# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:49:39 2020

@author: HP
"""


import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\lrm.xlsx")
plt.plot(data['Student_Population'],data['Restaurant'])

x=data['Student_Population']
y=data['Restaurant']

X = sm.add_constant(x)
model=sm.OLS(y,X)
result =model.fit()
print(result.summary())

reg = LinearRegression()
reg.fit(X,y)
print(reg)