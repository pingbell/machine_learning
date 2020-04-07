
"""
Created on Tue Apr  7 12:05:26 2020

@author: HP
"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as stats
import scipy.stats as statistics
""" alpha=0.05"""
data=pd.DataFrame({'C':[6,7,3,8],'M':[5,5,3,7],'E':[5,4,3,4] })
df = pd.melt(data.reset_index(),id_vars=['index'],value_vars=['C','M','E'])
df.columns =['index','treatments','value']

value_1 = statistics.f_oneway(data['C'],data['M'],data['E'])
Fcritical = statistics.f.ppf(.95,2,9)

model = stats.ols("value~C(treatments)",data=df).fit()
anova_table=sm.stats.anova_lm(model,typ=1)

""" accept null hypothesis"""