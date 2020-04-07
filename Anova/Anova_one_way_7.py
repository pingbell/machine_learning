# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:20:25 2020

@author: HP
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:05:26 2020

@author: HP
"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as stats
import scipy.stats as statistics
""" alpha=0.05"""
data=pd.DataFrame({'C':[10,15,11,10],'M':[9,7,5,6],'E':[20,16,10,14] })
df = pd.melt(data.reset_index(),id_vars=['index'],value_vars=['C','M','E'])
df.columns =['index','treatments','value']

value_1 = statistics.f_oneway(data['C'],data['M'],data['E'])
Fcritical = statistics.f.ppf(.95,2,9)

model = stats.ols("value~C(treatments)",data=df).fit()
anova_table=sm.stats.anova_lm(model,typ=1)
""" reject null hypothesis"""