# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:00:25 2020

@author: HP
"""




import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
data = pd.read_csv("E:\\DATASETS\\iriscsv\\Iris.csv")

df= data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
df= pd.melt(df.reset_index(),id_vars =['index'],value_vars=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
df.columns = ['index','Treatments','value']

import statsmodels.formula.api as smm
import statsmodels.api as st
model = smm.ols("value~C(Treatments)",data=df).fit()
anova_table = st.stats.anova_lm(model,typ=1)
Fcritical = stats.f.ppf(.99,3,596)