# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:15:10 2020

@author: Sharya prakash
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as stats
import scipy.stats as st


data = pd.read_excel("C:Users/HP/Desktop/data_analytics_with_python/oneway.xlsx")
"""['Black Board ', 'Case Presentation  ', 'PPT ']
"""

df=pd.melt(data.reset_index() ,id_vars = ['index'],value_vars = ['Black Board ', 'Case Presentation  ', 'PPT '])
df.columns = ['index','Treatements','value']
Fvalue =st.f_oneway(data['Black Board '], data['Case Presentation  '],data[ 'PPT '])[0]
pvalue =st.f_oneway(data['Black Board '], data['Case Presentation  '],data[ 'PPT '])[1]

F_critical = st.f.ppf(.95,2,6)

model = stats.ols("value ~C(Treatements)",data=df).fit()
anova_table = sm.stats.anova_lm(model,typ=1)
""" accept null hyp"""