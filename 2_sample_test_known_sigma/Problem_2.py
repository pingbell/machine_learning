# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:26:05 2020

@author: Shaurya Prakash 
"""
import numpy as np
import math
import scipy.stats as st
data1=[3,8,9,4,6]
data2=[4,7,6,3,5]
mean1= np.mean(data1)
mean2= np.mean(data2)
std1=np.std(data1)*(len(data1))/(len(data1)-1)
std2=np.std(data2)*(len(data2))/(len(data2)-1)

sp = (np.var(data1)*len(data1)+ np.var(data2)*len(data2))/(len(data1)+len(data2)-2)

std_error= sp*(1/len(data1)+1/len(data2))**.5

CI_low = (mean1-mean2)-st.t.ppf(.025,len(data1)+len(data2)-2)*std_error
CI_up = (mean1-mean2)+st.t.ppf(.025,len(data1)+len(data2)-2)*std_error
t= (mean1-mean2)/std_error