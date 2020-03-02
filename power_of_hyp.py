# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 23:54:08 2020

@author: HP
"""


# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt
import math
from scipy import stats

#popultaion
mu=170

#sample
sigma =10
n=25
xbar =172

 
"""
If, unknown to engineer, the true population mean were μ = 173,
 what is the probability that the engineer commits a Type II error?
"""
mu1 =173

x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
x1 = np.linspace(mu1 - 3*sigma, mu1 + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.plot(x1, stats.norm.pdf(x1, mu1, sigma))
plt.show()

def power(mu1,n,sigma) :
    return (1-stats.norm.cdf((mu1 -172)/(sigma/np.sqrt(n))))
 
print(power(mu1,n,sigma) )