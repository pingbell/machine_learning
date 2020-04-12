# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:50:36 2020

@author: Shaurya

H0 : mean1 = mean2
H1 : mean1!= mean2
"""
import numpy as np
import scipy.stats as st
data1= [.57,.34,.43,.32,.48,.40,.40]
data2= [.53,.47,.47,.51,.63,.61,.48]

std1=np.std(data1)*(len(data1))/(len(data1)-1)
std2=np.std(data2)*(len(data2))/(len(data2)-1)

mean1=np.mean(data1)
mean2=np.mean(data2)

alpha =0.05

sp=(std1*(len(data1)-1)+std2*(len(data2)-1))/(len(data1)+len(data2)-2)

z= (mean1-mean2)/sp*(1/len(data1) + 1/len(data1))**.5

zcritical= st.t.ppf(.05,(len(data1)+len(data2)-2))

interval_low = (mean1 -mean2)-zcritical*sp*(1/len(data1) + 1/len(data2))**.5
interval_high = (mean1 -mean2)+zcritical*sp*(1/len(data1) + 1/len(data2))**.5

# Accept null hypothesis