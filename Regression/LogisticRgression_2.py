# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:20:25 2020

@author: HP
"""
from sklearn.model_selection import train_test_split
from sklearn import linear_model 

from statsmodels.formula.api import ols
import statsmodels.api as sm

import pandas as pd
import numpy as np

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Week_9_Important_Data\\Simmons.xls")

"""basic summary functions"""
print(data.describe())
print(data.columns)
""" ['Customer', 'Spending', 'Card', 'Coupon'] """

#oneway anova -Method-1


df = pd.read_excel("C:Users/HP/Desktop/data_analytics_with_python/oneway.xlsx")
df_new = pd.melt(df.reset_index(),id_vars=['index'],value_vars=['Black Board ', 'Case Presentation  ', 'PPT '])
df_new.columns= ['index', 'Treatments', 'value']
OLS =ols("value~C(Treatments)",data=df_new).fit()
anova_table = sm.stats.anova_lm(OLS,typ=1)

#oneway anova -Method-2
import scipy.stats as stats
val=stats.f_oneway(df['Black Board '],df[ 'Case Presentation  '],df[ 'PPT '])


#oneway anova 



