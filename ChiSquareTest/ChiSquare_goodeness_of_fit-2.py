# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:32:10 2020

@author: Shaurya Prakash
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as stats
import scipy.stats as st

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\P_distribution.xlsx")
lambda_value = (data['Arrivals']*data['Frequency']).sum()/100
data['expected'] = data['Arrivals'].apply(lambda x : st.poisson.pmf(x,lambda_value)*100).apply(lambda x:np.round(x,decimals=2))
observed = [np.sum(data['Frequency'][0:3])]+list(data['Frequency'][3:])
expected =[np.sum(data['expected'][0:3])] +list(data['expected'][3:])

value = st.chisquare(observed,expected)
Fcritical=st.chi2.ppf(.95,7)

""" accept null hypothesis"""