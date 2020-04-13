# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 14:43:29 2020

@author: Shaurya Prakash

Two catalysts are being analyzed todetermine how they affect the mean
yield of a chemical process.
• Specifically, catalyst 1 is currently in use,but catalyst 2 is acceptable.
• Since catalyst 2 is cheaper, it should be adopted, providing it does not change
the process yield.
• A test is run in the pilot plant and results in the data shown in table.
• Is there any difference between the mean yields?
• Use 0.05, and assume equal variances.

Observation Catalyst 1 Catalyst 2
Number
1 91.50 89.19
2 94.18 90.95
3 92.18 90.46
4 95.39 93.21
5 91.79 97.19
6 89.07 97.04
7 94.72 91.07
8 89.21 92.75
𝑥 1= 92.255 
𝑥 1 = 92.733
s1 =2.39 s2 =2.9

H0 : mean1-mean2=0
H1 : mean1 != mean2 (ASSUMED UNEQUAL VARIANCES)
"""
import numpy as np
import math
import scipy.stats as st

data1 =[91.50,94.18,92.18,95.39,91.79,89.07,94.72,89.21 ]
data2 =[89.19,90.95,90.46,93.21,97.19,97.04,91.07,92.75 ]
mean1=np.mean(data1)
mean2=np.mean(data2)
std1 = np.std(data1)
std2 = np.std(data2)

dof =  ((std1**2/8) + (std2**2/8))**2/((std1**2/8)**2)/7 + ((std2**2/8)**2)/7

Z = (mean1-mean2)/np.sqrt( ((std1**2/8) + (std2**2/8)))
zritical_upper = st.t.ppf(.975,dof)
zritical_lower = st.t.ppf(.025,dof)

"""accepted null hyp."""

""" ASSUMING EQUAL VARIANCES HERE - WE USE POOLING"""

std_error = np.sqrt(((8-1)*std1**2 + (8-1)*std2**2)/(8+8-2)) *np.sqrt(1/8 +1/8)
bias = (mean1-mean2) -0
tscore=bias/std_error
df = 8+8-2

tritical_upper = st.t.ppf(.975,df)
tritical_lower = st.t.ppf(.025,df)
"""accepted null hyp."""

val= st.ttest_ind(data1,data2,equal_var=True)
""" accept null hyp"""