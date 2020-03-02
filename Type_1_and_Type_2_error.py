# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt
import math
from scipy import stats
"""
Created on Mon Mar  2 23:25:32 2020
The Brinell hardness scale is one of several definitions used in the field of materials science to quantify the hardness of a
piece of metal. The Brinell hardness measurement of a certain type of rebar used for reinforcing concrete and masonry 
structures was assumed to be normally distributed with a standard deviation of 10 kilograms of force per square millimeter. 
Using a random sample of n = 25 bars, an engineer is interested in performing the following hypothesis test:

the null hypothesis H0: μ = 170
against the alternative hypothesis HA: μ > 170
If the engineer decides to reject the null hypothesis if the sample mean is 172 or greater, that is, if 
¯
X
≥
172
, what is the probability that the engineer commits a Type I error?

Code @author: Shaurya 
Courtesy :https://online.stat.psu.edu/stat414/node/304/
"""
mu=170
sigma =10
n=25
xbar =172

def type_1_error(mu,sigma,n,xbar) :
    z_score = (Xbar-mu)/(sigma/np.sqrt(n))
    print( "rejection criteria is xbar>172 hence z>{}".format(z_score))
    return 1-stats.norm.cdf(1)

print(type_1_error(mu,sigma,n,xbar) )

"""
If, unknown to engineer, the true population mean were μ = 173,
 what is the probability that the engineer commits a Type II error?
"""
mu_1 =173
def type_2_error(mu_173,sigma,n,xbar) :
      z_score = (Xbar-mu_1)/(sigma/np.sqrt(n))
      return stats.norm.cdf(z_score)
print( type_2_error(mu_1,sigma,n,xbar) )    