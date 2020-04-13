"""
Created on Wed Apr  1 17:22:14 2020

@author:SHAURYA Prakash
H0 : fertilizer has no effect
H1: fertilizer affects athe yield.
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats 
from statsmodels.formula.api import ols
data= pd.DataFrame({"TA":[5,2,5,4,2],"TB":[3,3,0,2,2],"TC":[1,0,1,2,1]})
df= pd.melt(data.reset_index(),id_vars=['index'],value_vars=['TA','TB','TC'])
df.columns=['index','Treatments','value']

model = ols("value~C(Treatments)",data=df).fit()
anova_tabke = sm.stats.anova_lm(model,typ=1)

fcritical= stats.f.ppf(.95,2,12)

"""reject null """

from statsmodels.stats.multicomp import tukeyhsd
from statsmodels.stats.multicomp import MultiComparison

""" each group is of size 5 """
threshhold = 3.77*np.sqrt(1.433/6) 
"""     
TA     TC     = -2.6     
threshhold    = 3.77*np.sqrt(1.433/6) = 1.84
"""

mc= MultiComparison(df['value'],df['Treatments'])
result = mc.tukeyhsd(0.05) 
print(result.summary())


"""TA and TC are different"""