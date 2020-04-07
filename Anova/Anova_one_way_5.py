# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:41:15 2020

@author: Shaurya Prakash
"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as stats
import scipy.stats as statistics
""" alpha=0.05"""
data=pd.DataFrame({'C':[9,10,13,9,9],'M':[12,13,11,14,5],'E':[17,17,15,9,7],'I':[13,12,12,18,15]})

value_1 = statistics.f_oneway(data['C'],data['M'],data['E'],data['I'])

""" p-value>Alpha ,accept null hypothesis"""

#OLS-method
df= pd.melt(data.reset_index(),id_vars=["index"],value_vars=["C","M","E","I"])
df.columns=['index','treatments','value']
model =stats.ols("value~C(treatments)",data=df).fit()
anova_table = sm.stats.anova_lm(model,typ=1)

Fcrtitical = statistics.f.ppf(.95,3,16)
""" F<Fcrtitical , accept null hypothesis"""