# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:29:23 2020

@author: Shaurya Prakash

Arsenic concentration in public drinking water supplies is a potential health risk.
• An article in the Arizona Republic (Sunday, May 27, 2001) reported
drinking water arsenic concentrations in parts per billion (ppb) for 10 metropolitan Phoenix
communities and 10 communities in rural Arizona. • The data as shown:5 
Metro Phoenix Rural Arizona
Phoenix, 3 Rimrock, 48
Chandler, 7 Goodyear, 44
Gilbert, 25 New River, 40
Glendale, 10 Apachie Junction, 38
Mesa, 15 Buckeye, 33
Paradise Valley, 6 Nogales, 21
Peoria, 12 Black Canyon City, 20
Scottsdale, 25 Sedona, 12
Tempe, 15 Payson, 1
Sun City, 7 Casa Grande, 18
𝑥 1 = 12.5 𝑥 1 = 27.5
s1 =7.63 s2 =15.3

H0 : mean1 = mean2
H1 : mean1!= mean2
"""
import numpy as np
s1 =7.63 
s2 =15.3
import scipy.stats as st
data1=[3,7,25,10,15,6,12,25,15,7]
data2=[48,44,40,38,33,21,20,12,1,18]
val = st.ttest_ind(data1,data2,equal_var=False)
dof =  ((s1**2/10) + (s2**2/10))**2/(((s1**2/10)**2)/9 + ((s2**2/10)**2)/9 )
tcritical = st.t.ppf(.025,dof)
"""reject null"""

