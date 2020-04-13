# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 14:45:14 2020

@author: Shaurya Prakash
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as stats
import scipy as sp

data = pd.DataFrame({'A':[5,3,4,0,3],'B':[4,3,3,6,4],'C':[6,7,3,4,5]})
df1= pd.melt(data.reset_index(),id_vars=['index'],value_vars=['A','B','C'])
df1.columns=['index','Treatments','value']

#one way anova
model = stats.ols("value~C(Treatments)",data=df1).fit()
anova_table = sm.stats.anova_lm(model,typ=1)

#RBD
df2= pd.melt(data.reset_index(),id_vars=['index'],value_vars=['A','B','C'])
df2.columns=['block','Treatments','value']
model_RBD = stats.ols("value~C(Treatments)+C(block)",data=df2).fit()
anova_table_RBD = sm.stats.anova_lm(model_RBD,typ=1)

#Two way
df3 = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\Twoway.xlsx")
 
model=st.ols("Value~C(college)+C(prep_pro)+C(college):C(prep_pro)",data=df3).fit()
anova_table_2way = sm.stats.anova_lm(model,typ=2)