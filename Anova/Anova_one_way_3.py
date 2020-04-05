# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:03:32 2020

@author:Shaurya Prakash

An experiment was performed to determine the effect of four different
chemicals on the strength of a fabric.
• These chemicals are used as part of the permanent press finishing
process.
• Five fabric samples were selected, and a randomized complete block
design was run by testing each chemical type once in random order on
each fabric sample.
• The data are shown in Table.
• We will test for differences in means using an ANOVA with alpha = 0.01.

no of treatments = 4 , dof =3
no of blocks =5   , dof = 4
sse_dof = 3x4 =12
desired value of F = print(st.f.ppf(.99,3,12))=5.952544681545868
Reject null hypotheses if F-value is greater than 5.952544681545868.

"""
import scipy.stats as st
F_crtitcal = st.f.ppf(.99,3,12)

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\rbd2.xlsx")

df= pd.melt(data.reset_index(),id_vars=["index"],value_vars=['chem1', 'chem2', 'chem3', 'chem4'])
df.columns=['fabric','chemical','value']

from statsmodels.formula.api import ols
model1 =ols("value~C(chemical)",data=df).fit()
import statsmodels.api as sm
anova_table1 = sm.stats.anova_lm(model1,typ=1)

from statsmodels.formula.api import ols
model =ols("value~C(chemical)+C(fabric)",data=df).fit()
import statsmodels.api as sm
anova_table = sm.stats.anova_lm(model,typ=1) # F=75.89484752891696

"""Reject Null Hypothesis : 75.89484752891696 > 5.952544681545868
chemical has effect on four different fabric.
"""
 