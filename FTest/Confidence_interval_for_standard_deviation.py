# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:38:43 2020

@author: Shaurya Prakash
"""

import numpy as np
from scipy import stats

sample1 = [8260,8130,8350,8070,8340]
sample2 = [7950,7890,7900,8140,7920,7840]
var1    = np.var(sample1,ddof=1)
var2    = np.var(sample2,ddof=1)
aplha   = 0.01
mean1   = np.mean(sample1)
mean2   = np.mean(sample2)
n1      = len(sample1)
n2      = len(sample2)
""" 
h0 = mu1-mu2 =0
h1 = mu1!=mu2
"""
print(stats.ttest_ind(sample1,sample2,equal_var=True))
print(stats.ttest_ind(sample1,sample2,equal_var=False))
dof     = len(sample1)+len(sample2)-2
spooled = np.sqrt( ((n1-1)*var1 +(n2-1)*var2)/dof )
confidence_interval = (stats.t.ppf(0.005,8),stats.t.ppf(0.995,8))

print("reject ho" ) 

""" estimate sigma """ 
chi_square_right = (n2-1)*var2/chi2.isf(q=.005,df=5)
chi_square_left =  (n2-1)*var2/chi2.isf(q=.995,df=5)

cnfidence_interval_sigma = (np.sqrt(chi_square_left),np.sqrt(chi_square_right))
print(cnfidence_interval_sigma)





