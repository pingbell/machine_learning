# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 14:19:04 2020
@author: Shaurya Prakash
"""
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model

df = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Week_9_Important_Data\\Simmons.xls") 
print(df.describe())

X = df[[ 'Spending', 'Card']]

y =df['Coupon'].values.reshape(-1,1)

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,y,random_state=42,test_size=.25)
""" Index(['Customer', 'Spending', 'Card', 'Coupon'], dtype='object') """
df.Coupon.values

model = linear_model.LogisticRegression(solver='lbfgs')
model.fit(Xtrain,Ytrain.ravel())
ypredict = model.predict(Xtest)

PREDICT_PROB_Train = model.predict_proba(Xtrain)[:,1]
PREDICT_PROB_Test = model.predict_proba(Xtest)[:,1]


