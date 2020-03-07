# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 23:27:59 2020

@author: Shaurya Prakash 
"""
import numpy as np
from scipy import stats 
sample1 = [14.4,14.2,14.4,14.3,14.6]
n=5
var = np.var(sample1,ddof =1)
mean =np.mean(sample1)

chi_square_upper = stats.chi2.isf(q=.005,df=4)
chi_square_lower = stats.chi2.isf(q=.995,df=4)
CL = ((n-1)*var/chi_square_upper) ,((n-1)*var/chi_square_lower) 
print(CL)