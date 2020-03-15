# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:57:36 2020

@author: Shaurya Prakash
"""
import pandas as pd 
import numpy as np 
from scipy import stats 
from statsmodels.formula.api import ols 
import statsmodels.api as sm



sample1=[75,74,70,73,76,73]
sample2=[76,74,71,72,73,73]
sample3=[78,74,75,77,76,73]
data = pd.DataFrame({"tr1" : sample1 ,"tr2" : sample2,"tr3" : sample3})


data_new = pd.melt(data.reset_index(),id_vars=['index'],value_vars=['tr1','tr2','tr3'])
data_new.columns = ['index','treatments','value']
model = ols('value ~  C(treatments)' ,data = data_new).fit()
anova_table = sm.stats.anova_lm(model,typ=1)

data_new_1 = pd.melt(data.reset_index(),id_vars=['index'],value_vars=['tr1','tr2','tr3'])
data_new_1.columns = ['blocks','treatments','value']
model_1 = ols('value ~   C(treatments) + C(blocks)' ,data = data_new_1).fit()
anova_table_1 = sm.stats.anova_lm(model_1,typ=1)

print(stats.f_oneway(sample1,sample2,sample3))
oneway = stats.f_oneway(sample1,sample2,sample3)