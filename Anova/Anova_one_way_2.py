# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:42:09 2020

@author: HP
"""
import pandas as pd
import statsmodels.formula.api as sm
import statsmodels.api as an
import scipy.stats as stats
from matplotlib import pyplot as plt


data = pd.read_excel("C:Users/HP/Desktop/data_analytics_with_python/oneway.xlsx")
print(data.columns)
plt.plot(data)
plt.show()

"""ONEWAY ANOVA"""
data.columns = ["Treatment1","Treatment2","Treatment3"]
oneway_result=stats.f_oneway(data["Treatment1"],data["Treatment2"],data["Treatment3"])

"""ONEWAY ANOVA"""
data_new= pd.melt(data.reset_index(),id_vars=['index'],value_vars=["Treatment1","Treatment2","Treatment3"])
data_new.columns=["index","Treatment","value"]
model = sm.ols("value~C(Treatment)",data=data_new).fit()
anova= an.stats.anova_lm(model,typ=1)
f = stats.f.ppf(.95,2,6)
""" accept null hypothesis"""
"""ONEWAY ANOVA"""
 
model1 = sm.ols("value~C(Treatment)+C(index)",data=data_new).fit()
anova1= an.stats.anova_lm(model1,typ=1)
 


