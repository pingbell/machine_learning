# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:13:04 2020

@author: shaurya prakash
A company manufactures impellers for use in jet-turbine engines.
• One of the operations involves grinding a particular surface finish on a
titanium alloy component.
• Two different grinding processes can be used, and both processes can produce
parts at identical mean surface roughness.
• The manufacturing engineer would like to select the process having the least
variability in surface roughness.
• A random sample of n1 =11 parts from the first process results in a sample
standard deviation s1 = 5.1 micro inches, and a random sample of n2 = 16
parts from the second process results in a sample standard deviation of s2 =
4.7 micro inches.
• We will find a 90% confidence interval on the ratio of the two standard
deviations.
ho : mean1=mean2
h1 : mean1!= mean2 
"""
import numpy as np
import scipy.stats as st

n1 =11
s1=5.1
n2=16
s2=4.7

Ftest = s1**2/s2**2

Fcitical = st.f.ppf(.95,10,15)

F_low = st.f.ppf(.05,10,15)*Ftest
F_up = st.f.ppf(.95,10,15)*Ftest

""" accept null """


