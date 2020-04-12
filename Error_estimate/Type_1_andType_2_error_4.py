# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 21:43:08 2020

@author: Shaurya Prakash

Question 3.

The mean response time for a random sample of 40 foodorder is 13.25 minutes
• The population standard deviation is believed to be 3.2
minutes.
• The restaurant owner wants to perform a hypothesis test,
with  =0.05 level of significance, to determine whether the
service goal of 12 minutes or less is being achieved


ho: mean=12
h1: mean<12
"""

n=40
sigma=3.2
alpha= 0.05
mean1=12 

standard_error = sigma/np.sqrt(n)
max_error = st.norm.ppf(.95)*standard_error
X_value = mean1 + max_error
Zvalue = np.sqrt(n)*(X_value - 13.25 )/sigma
beta = st.norm.cdf(Zvalue)

