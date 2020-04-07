# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:15:02 2020

@author: Shaurya Prakash
"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as stats
import scipy.stats as staitistics

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\Twoway.xlsx")
 
model=stats.ols("Value~C(college)+C(prep_pro)+C(college):C(prep_pro)",data=data).fit()
anova_table = sm.stats.anova_lm(model,typ=2)

model = stats.ols("Value~C(college)",data=data).fit()
simple_anova = sm.stats.anova_lm(model,typ=1)

model_RBD = stats.ols("Value~C(college)+C(prep_pro)",data=data).fit()
simple_anova_RBD = sm.stats.anova_lm(model_RBD,typ=1)