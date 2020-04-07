# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:17:31 2020

@author: Shaurya Prakash
"""
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as statistics
import numpy as np
from statsmodels.stats.outliers_influence import summary_table 
data= pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\icecream.xlsx")
sns.regplot(data['Student_Population'],data['Sales'],fit_reg=True)


