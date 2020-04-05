# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:10:09 2020

@author:Shaurya Prakash

• A team of engineers responsible for the study decides to investigate four
levels of hardwood concentration: 5%, 10%, 15%, and 20%.
• They decide to make up six test specimens at each concentration level,
using a pilot plant.
• All 24 specimens are tested on a laboratory tensile tester, in random order.
The data from this experiment are shown in Table 
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\Tensile_strength_o_ paper.xlsx")
"""['hardwood concentration 5%', 
    'hardwood concentration 10%',
    'hardwood concentration 15%', 
    'hardwood concentration 20%'
   ]
"""
df= pd.melt(data.reset_index(),id_vars=['index'],value_vars=['hardwood concentration 5%', 
                                                            'hardwood concentration 10%',
                                                            'hardwood concentration 15%', 
                                                            'hardwood concentration 20%'
                                                           ])
df.columns=['index','Treatments','value']
plt.boxplot([data['hardwood concentration 5%'],data['hardwood concentration 10%'],data['hardwood concentration 15%'],data['hardwood concentration 20%']])

import scipy.stats as statistics
vals=statistics.f_oneway(data['hardwood concentration 5%'],data['hardwood concentration 10%'],data['hardwood concentration 15%'],data['hardwood concentration 20%'])
f_value=stats.f.ppf(.99,3,20)
 
import statsmodels.api as sm
import statsmodels.formula.api as stat
model= stat.ols("value~C(Treatments)",data=df).fit()
anova_table = sm.stats.anova_lm(model,typ=1)

#LSD Test
MSE =6.508333333333333

t_alpha_by_2_dof_20=statistics.t.ppf(.005,20) """alpha/2 in argument"""
n=6
LSD =np.abs( t_alpha_by_2_dof_20*np.sqrt(2*MSE/n))
print(LSD)

#TukeysTest
from  statsmodels.stats.multicomp import MultiComparison
from  statsmodels.stats.multicomp import pairwise_tukeyhsd
mc= MultiComparison(df['value'],df['Treatments'])
mc_result = mc.tukeyhsd(0.01)
print(mc_result.summary())

