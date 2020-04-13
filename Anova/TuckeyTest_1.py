# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 23:31:23 2020

@author: Shaurya Prakash
"""
import numpy as np
import pandas as pd
from  statsmodels.formula.api import ols
import statsmodels.api as sm
import scipy.stats as st

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\cotton.xlsx")
df=pd.melt(data.reset_index(),id_vars=['index'],value_vars=['cotwt.15', 'cotwt.20', 'cotwt.25', 'cotwt.30', 'cotwt.35'])
df.columns = ['index','Treatment','value']
model = ols("value~C(Treatment)",data= df).fit()
anova_table = sm.stats.anova_lm(model,typ=1)
Fcritical = st.f.ppf(.95,4,20)

"""Reject  Null Hypothesis """

""" post hoc analysis """

from statsmodels.stats.multicomp import MultiComparison
from statsmodels.stats.multicomp import tukeyhsd

mc = MultiComparison(df['value'],df['Treatment'])
result =mc.tukeyhsd(.05)
print(result.summary())

""" each sample size is same 5"""

threshhold = 4.23 * np.sqrt(8.06*(1/5))

