# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:06:20 2020

@author: HP
"""
import scipy.stats as st
import numpy as np
import math

"""
Ho: µ = 8.3
H1: µ < 8.3
Determine the probability of Type II error,
if µ = 7.4 at 5% significance level. σ = 3.1 and n = 60.
Left handed test.


solution :
1.for distribution centerd at 8.3 ,
z_critical_left = mu - z_alpha x sigma/sqrt(n) 
 
"""

Z_alpha_05 = -st.norm.ppf(.05)

standard_error = Z_alpha_05*3.1/np.sqrt(60)

X_value = 8.3-standard_error

Z_value =np.sqrt(60)* ( X_value-7.4 )/3.1

beta = 1-st.norm.cdf(Z_value) #Type 2 error