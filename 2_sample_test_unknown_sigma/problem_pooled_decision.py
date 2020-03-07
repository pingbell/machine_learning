# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:09:53 2020
@author: Shaurya Prakash
"""
import numpy as np
from scipy import stats 

sample1=[66.3,63.5,64.9,61.8,64.3,64.7,65.1,64.5,68.4,63.2]
sample2=[71.3,60.4,62.6,63.9,68.8,70.1,64.8,68.9,65.8,66.2]

variance1 = np.var(sample1)
variance2 = np.var(sample2)

std1 = np.sqrt(variance1)
std2 = np.sqrt(variance2)
n1=len(sample1)
n2=len(sample2)
dof = np.floor(((variance1/n1 + variance2/n2)**2)/ ((((variance1/n1)**2 )/(n1-1))+ (((variance2/n2)**2)/(n2-1))) )
    

""" test for significant differnce of means at aplha 0.05 
h0 : mu1=mu2
h1 : mu1-mu2<0 (lower tailed test)
"""
critical_value = stats.t.ppf(0.05,dof)
statistics,pvalue     = (stats.ttest_ind(sample1,sample2,equal_var=False))
alpha =0.05


def isPooling(variance1,variance2) :
    if (((variance1/variance2 )> 4) |((variance1/variance2)<.25)):
        return True 
    else :
        return False


def isReject_lower_tailed_test (aplha_limit,pvalue) :
    if(aplha_limit>pvalue) :
        return True
    else:
        return False

def isReject_lower_tailed_test_crit (critical_value,statistics) :
    if(critical_value>statistics) :
        return True
    else:
        return False
    

print(stats.t.cdf(-1.300394907012252,18))
print((stats.ttest_ind(sample1,sample2,equal_var=False)))
print("Is pooling required ={}".format(isPooling(variance1,variance2)))
print("pvalue approach : is rejected ={}".format(isReject_lower_tailed_test (alpha,pvalue)))
print("critical approach : is rejected ={}".format(isReject_lower_tailed_test_crit(critical_value,statistics)))
print("dof ={}".format(dof))
print("\n\n\n")



""" question bit 2
mu1 - mu2 = 0
mu1 != mu2
"""

bumper1 =[407,448,423,465,402,419]
bumper2 =[434,415,412,451,433,429]
alpha =0.01

n1_1=6
n2_1=6
variance1_1 = np.var(bumper1)
variance2_1 = np.var(bumper2)

dof_1 = np.floor(((variance1_1/n1_1 + variance2_1/n2_1)**2)/ ((((variance1_1/n1_1)**2 )/(n1_1-1))+ (((variance2_1/n2_1)**2)/(n2_1-1))) )
   
confidence_interval_1 = (stats.t.ppf(.005,8),stats.t.ppf(.995,8))
statistics_1,pvalue_1     = (stats.ttest_ind(bumper1,bumper2,equal_var=False))

print("Is pooling required ={}".format(isPooling(np.var(bumper1),np.var(bumper2) )))
print(stats.ttest_ind(bumper1,bumper2,equal_var=False))
print("confidence interval = {}".format(confidence_interval))
print("dof_1 ={}".format(dof_1))


