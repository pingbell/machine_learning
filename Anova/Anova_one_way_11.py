# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:22:14 2020

@author:SHAURYA Prakash
H0 : fertilizer has no effect
H1: fertilizer affects athe yield.
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats 
from statsmodels.formula.api import ols

data = pd.read_csv("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\crop.csv")
df= data[['fertilizer','yield']] 
df.columns=['treatment','value']

model = ols("value ~ C(treatment)",data=df).fit()

anova_lm = sm.stats.anova_lm(model,typ=1)

fcritical = stats.f.ppf(.95,2,93)

""" accept null hypothesis """


