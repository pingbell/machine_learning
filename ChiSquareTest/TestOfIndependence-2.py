# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:11:55 2020

@author: Shaurya Prakash
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as stats

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\acad.xlsx")
table=pd.pivot_table(data[['sm','g']],index='g',columns='sm',aggfunc=len)

import scipy.stats as st
chi2val,p,dof,tbl= st.chi2_contingency(table) #f=2.36
F_critical1 = st.chi2.ppf(.99,2) # 9.21
""" accept null hypothesis """
 
