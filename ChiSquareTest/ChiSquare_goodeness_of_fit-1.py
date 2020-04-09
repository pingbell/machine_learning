# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:50:52 2020

@author: Shaurya Prakash
"""
import numpy as np
import pandas as pd
import scipy.stats as stats

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\P_distribution.xlsx")

lambda_value= (data['Arrivals']*data['Frequency']).sum()/data.Frequency.sum()
expected_frequency = data['Arrivals'].apply(lambda x: 100*stats.poisson.pmf(lambda_value,x))
data['expected_frequency'] =expected_frequency
expec= [1.25]+list(expected_frequency[3:])
observerd = [(data['Frequency'][0]+data['Frequency'][1]+data['Frequency'][2])] +list(data.Frequency[3:])
final = stats.chisquare(expec,observerd)
F= stats.chi.ppf(.95,7)

"""reject null"""