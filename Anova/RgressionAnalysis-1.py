# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:17:31 2020

@author: Shaurya Prakash
"""
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as statistics
import numpy as np
from statsmodels.stats.outliers_influence import summary_table
 
data= pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\icecream.xlsx")
sns.regplot(data['Student_Population'],data['Sales'],fit_reg=True)

x=data['Student_Population']
y=data['Sales']

model=sm.OLS(data['Sales'],sm.add_constant(data['Student_Population']))
result1= model.fit()
print(result1.summary())

st,data,ss2 = summary_table(result1,alpha=0.05)
fitted_value=data[:,:2]
predicted_mean_se = data[:,3]
predicted_mean_ci_low,predicted_mean_ci_upper=data[:,4:6].T
predicted_ci_low,predicted_ci_upper=data[:,6:8].T

 
fig,ax= plt.subplots(figsize=(8,6))
ax.plot(data['Student_Population'],data['Sales'])
ax.plot(X,predicted_mean_ci_low,'g--')
ax.plot(X,predicted_mean_ci_upper,'g--')
ax.plot(X,predicted_ci_upper,'b--')
ax.plot(X,predicted_ci_low,'b--')