# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:46:49 2020

@author: shauyra prakash
"""
import pandas as np
from statsmodels.formula.api import ols
from scipy import stats
import statsmodels.api as sm 

data = pd.read_excel("C:Users/HP/Desktop/data_analytics_with_python/oneway.xlsx")
print(data.columns)
data_new = pd.melt(data.reset_index(),id_vars=["index"],value_vars=['Black Board ', 'Case Presentation  ', 'PPT '])
data_new.columns = ["Block","Treatments","value"]
model = ols("value ~C(Treatments) +C(Block)",data= data_new).fit()
anova_table = sm.stats.anova_lm(model,typ=1)