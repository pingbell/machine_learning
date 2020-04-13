# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:29:28 2020

@author: Shaurya Prakash
"""
"""
The cutting speeds of four types of tools are being compared in an experiment. Five cutting materials
of varying degree of hardness are to be used as experimental blocks. The data giving the measurement
of cutting time in seconds appear in the table below
Block Treatment
Treatment 1  2 3 4 5      Means
       1  12 2 8 1 7     x¯T1 =6
       2  20 14 17 12 17 x¯T2 =16
       3  13 7 13 8 14   x¯T3 =11
       4  11 5 10 3 6    x¯4 =7
Block Means x¯B1 =14 ¯xB2 =7 ¯xB3 =12 ¯xB4 =6 ¯xB5 =11 x¯ =10
"""
data = pd.DataFrame({"A" :[12,2,8,1,7] ,
                     "B" :[20,14,17,12,12],
                     "C" :[13,7,13,8,14],
                     "D" :[11,5,10,3,6]})
df= pd.melt(data.reset_index(),id_vars=['index'],value_vars=['A', 'B', 'C', 'D'])
df.columns =['blocks','Treatment','value']
from statsmodels.formula.api import ols
model =ols("value~C(Treatment)+C(blocks)",data=df).fit()
import statsmodels.api as sm
anova_table = sm.stats.anova_lm(model,typ=1)
from scipy import stats as st
threshold = st.f.ppf(.95,3,17)

"""reject null """
