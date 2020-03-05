# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:30:55 2020

@author: HP
"""
import numpy as np
import pandas as pd
from scipy import stats 

"""
sample type = small
variance = unknown
sigma1 != sigma2
pooling = if s1_square>4*s2_square then  should not pool.
test = T-test
ho=
h1=
"""

"""
problem statement : 
    sample1=[3,7,25,10,15,6,12,25,7]
    sample2=[48,44,40,38,33,21,2,12,1,18]
    alpha =0.05
    mean volume of sample2 is less than sample1.
    ho :mu1-mu2=0
    h1 :mu1 != mu2
"""
n1 = 9
n2 = 10
alpha = 0.05
sample1=[3,7,25,10,15,6,12,25,7]
sample2=[48,44,40,38,33,21,2,12,1,18]
s1_square = np.var(sample1)
s2_square = np.var(sample2)

def accept_or_reject(alpha,zscore) :
    if ((stats.t.ppf(alpha,12)>zscore) | (stats.t.ppf((1-alpha),12)<zscore)):
       return "reject Ho"
    else :
       return "Accept Ho"
        
def is_pooling_required(s1_square,s2_square) :
    if ((s1_square>4*s2_square) | (4*s1_square<s2_square)) :
        return False
    else :
        return True 
    
def dof(sample1,sample2):
    degree_of_freedom = (((s1_square/n1)+(s2_square/n2))**2)/(((s1_square/n1)**2)/(n1-1)+((s2_square/n2)**2)/(n2-1))
    return np.floor(degree_of_freedom)

"""STATISTICS"""

print(stats.ttest_ind(sample1,sample2,equal_var=False))
print(accept_or_reject(alpha,stats.ttest_ind(sample1,sample2,equal_var=False)[0]))
print("alpha = {}.".format(stats.t.ppf(0.025,12)))

"""STATISTICS"""




