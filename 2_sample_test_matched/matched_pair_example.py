# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:38:01 2020

@author: Shaurya Prakash
"""
import numpy as np
import pandas as pd
from scipy import stats

sample1=[1.186,1.151,1.322,1.339,1.200,1.402,1.365,1.537,1.559]
sample2=[1.061,0.992,1.063,1.062,1.065,1.178,1.037,1.086,1.052]
diff =[]
alpha =0.05

"""
ho : sample1 and sample2 has no same. mu1-mu2 = 0
h1 : sample1 and sample2 are different. mu1 - mu2 !=0
"""
for i,j in zip(sample1,sample2) :
    diff.append(np.round((i-j),3))
t_alpha = 0.025
t_score,p_value = stats.ttest_rel(sample1,sample2)

def accept_or_reject(t_alpha,zscore,dof) :
    if ((stats.t.ppf(t_alpha,dof)>zscore) | (stats.t.ppf((1-t_alpha),dof)<zscore)):
       return "reject Ho"
    else :
       return "Accept Ho"
print(accept_or_reject(t_alpha,t_score,len(sample1)-1))    

"""
staistics 

"""
