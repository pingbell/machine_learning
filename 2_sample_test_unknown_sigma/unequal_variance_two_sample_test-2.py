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
    sample1=[0.63,2.64,1.85,1.68,1.9,1.67,0.73,1.04,0.68]
    sample2=[3.71,4.09,4.11,3.75,3.49,3.27,3.72,3.49,4.26]
    alpha =0.05
    mean volume of sample2 is less than sample1.
    ho :mu1-mu2=0
    h1 :mu1 != mu2
"""
n1 = 9
n2 = 9
alpha = 0.05
sample1=[0.63,2.64,1.85,1.68,1.9,1.67,0.73,1.04,0.68]
sample2=[3.71,4.09,4.11,3.75,3.49,3.27,3.72,3.49,4.26]
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

zscore =stats.ttest_ind(sample1,sample2,equal_var=False)[0]
pvalue=stats.ttest_ind(sample1,sample2,equal_var=False)[1]
zalpha_left = stats.t.ppf(0.025,11)
zalpha_right = stats.t.ppf(1-0.025,11)
print("Pooling is required ={}".format(is_pooling(s1_square,s2_square)))
print("zscore = {}".format(zscore))
print("pvalue = {}".format(pvalue))
print("zalpha_left = {}".format(zalpha_left))
print("zalpha_right = {}".format(zalpha_right))
print(accept_or_reject(alpha,zscore) )





