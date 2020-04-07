# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:45:54 2020

@author: Shaurya Prakash
"""
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as statistics
data= pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\regr.xlsx")

x= data['TV Ads']
y= data['car Sold']

i = sm.add_constant(x)
model= sm.OLS(y,i)
result= model.fit()
print(result.summary())
plt.scatter(x,y)
plt.scatter(np.mean(x),np.mean(y),color="red")
sns.regplot(x,y,fit_reg=True)

val1=5+statistics.t.ppf(0.025,3)*1.08
val2=5+statistics.t.ppf(0.975,3)*1.08
Fstats=statistics.f.ppf(.95,1,4)