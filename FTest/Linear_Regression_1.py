# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:04:46 2020

@author: Shaurya Prakash
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm

dependent_var =[20,45,56,34,28,49]
independent_var =  sm.add_constant([1,3,5,2,1.6,3.7])
model =sm.OLS(dependent_var,independent_var)
result = model.fit()
print(result.summary())



