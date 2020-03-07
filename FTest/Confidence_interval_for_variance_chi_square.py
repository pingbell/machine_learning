# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:27:27 2020

find out confidence interval for variance when sample variance is to be compared with 
population variance.

@author: Shaurya Prakash
"""

import numpy as np
from scipy import stats
from scipy.stats import chi2

""" example 1  : n=51 , find CL for variance with alpha =0.05 """

n=51 
sample_variance = 2

chi_left = chi2.isf(q=0.975, df=50)
chi_right = chi2.isf(q=.025,df=50)

Cl_alpha_05 = ( ((n-1)*(sample_variance)/chi_right) ,((n-1)*(sample_variance)/chi_left))
print(Cl_alpha_05)

""" example2 : n=20 compute the confidence interval for 95 % CL , sigma = 0.000120"""

n = 20
sample_variance = 0.000120 

chi_right= chi2.isf(q=0.025,df =19)
chi_left = chi2.isf(q=0.975,df =19)
Cl_alpha_05_sample = ( ((n-1)*(sample_variance)/chi_right) ,((n-1)*(sample_variance)/chi_left))
Cl_alpha_05_sample_std = ( np.sqrt((n-1)*(sample_variance)/chi_right) ,np.sqrt((n-1)*(sample_variance)/chi_left))

print("confidence interval for variance ={}".format(Cl_alpha_05_sample))
print("confidence interval for standard deviation ={}".format(Cl_alpha_05_sample_std))
