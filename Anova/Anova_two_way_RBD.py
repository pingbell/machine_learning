# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:46:49 2020

@author: shauyra prakash
"""
import statsmodels.api as sm
import statsmodels.formula.api as stats
from scipy import stats as scstats
import pandas as pd
data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\Twoway.xlsx")

model =ols("Value~C(college)+C(prep_pro)+C(college):C(prep_pro)",data=data).fit()
anova_table=sm.stats.anova_lm(model,typ=2)
print(scstats.f.ppf(.95,2,9))
 
 

