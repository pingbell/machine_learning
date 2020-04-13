# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:48:57 2020

@author: HP
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as st
import scipy.stats as stats

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\Twoway.xlsx")
 
model=st.ols("Value~C(college)+C(prep_pro)+C(college):C(prep_pro)",data=data).fit()
anova_table = sm.stats.anova_lm(model,typ=2)

 