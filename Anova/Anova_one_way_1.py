# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:22:14 2020

@author:SHAURYA Prakash
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats 
from statsmodels.formula.api import ols

data = pd.read_excel("C:Users/HP/Desktop/data_analytics_with_python/oneway.xlsx")
print(data.columns)
data_new = pd.melt(data.reset_index(),id_vars=['index'],value_vars=['Black Board ', 'Case Presentation  ', 'PPT '])

data_new.columns = ["index" ,"Treatments","value"]
model = ols("value~C(Treatments)" , data= data_new).fit()
anova_tabel = sm.stats.anova_lm(model,typ=1)

"Accept the null hypothesis"
