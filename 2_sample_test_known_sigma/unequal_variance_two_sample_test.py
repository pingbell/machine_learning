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

"""Predefined methods"""
print(stats.t.ppf(0.025,11))
print(stats.ttest_ind(sample1,sample2,equal_var=False))

"""Predfined Methods End Here """

""" User Defined"""
def is_pooling(s1_square,s2_square) :
    if ((s1_square>4*s2_square) | (4*s1_square<s2_square)) :
        return False
    else :
        return True 
print("Pooling is required ={}".format(is_pooling(s1_square,s2_square)))

def zscore(sample1,sample2):
    zscore =  (np.mean(sample1)-np.mean(sample2) )/(np.sqrt((s1_square/n1)+(s2_square/n2)))
    degree_of_freedom = (((s1_square/n1)+(s2_square/n2))**2)/(((s1_square/n1)**2)/(n1-1)+((s2_square/n2)**2)/(n2-1))
    return (zscore,np.floor(degree_of_freedom))

print(zscore(sample1,sample2))
""" User Defied nds Here """


