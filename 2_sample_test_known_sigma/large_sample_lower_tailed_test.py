# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 22:33:37 2020

@author: Shaurya Prakash
"""
import numpy as np
from scipy import stats 
import math

"""                          _________sigma1 and sigma2 known[Z-test]    _________ sigma1  = sigma2[ T-test (unknown sigmas) +pooling]
    test for means ---------|_________sigma1 and sigma2 not known-------|________  sigma1 != sigma2[Ttest(unknown sigmas) + dof]
    large sample means n>=30  
    standard deviation is sigma1 , sigma2 are known  = ZTEST
"""

""" Problem Statement :
• A product developer is interested in reducing the drying time of a primer paint.
• Two formulations of the paint are tested; formulation 1 is the standard chemistry, and
formulation 2 has a new drying ingredient that should reduce the drying time.
• From experience, it is known that the standard deviation of drying time is 8 minutes, and this
inherent variability should be unaffected by the addition of the new ingredient.
• Ten specimens are painted with formulation 1, and another 10 specimens are painted with
formulation 2; the 20 specimens are painted in random order.
• The two-sample average drying times are 𝑥1 = 121 minutes and 𝑥2 = 112 minutes,
respectively.
• What conclusions can the product developer draw about the effectiveness of the new
ingredient, using alpha = 0.05?

"""
sigma  = 8
sigma1 = 8
sigma2 = 8   

n1=10
n2=10
x1bar=121
x2bar=112

alpha =0.05

ho = "mu1=mu2"
h1 = "mu1>mu2"
test_type ="right_tailed_test [ZSCORE]"

def right_tailed_test(sigma,n1,n2,x1bar,x2bar):
    zscore = ((x1bar -x2bar) -0)/np.sqrt((sigma*sigma)/n1 + (sigma*sigma)/n2)
    return zscore


def evaluate(zscore,alpha) :
    if(zscore >stats.norm.ppf(1-alpha)) :
        print ("Reject ho for aplha= {}".format(alpha))
    else :
        print("Accep ho for aplha= {}".format(alpha))
zscore=right_tailed_test(sigma,n1,n2,x1bar,x2bar)
print(zscore)
evaluate(zscore,alpha)