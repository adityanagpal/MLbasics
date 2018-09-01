#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:02:15 2018

@author: aditya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('kc_house_data.csv')

X=dataset.iloc[:,[3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20]].values
y=dataset.iloc[:,2].values

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

import statsmodels.formula.api as sm
X=np.append(arr=X,values=np.ones((21613,1)).astype(int),axis=1)
#significance level = 0.05
Xopt=X[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]]
regressor_OLS=sm.OLS(endog=y,exog=Xopt).fit()
regressor_OLS.summary()

Xopt=X[:,[0,1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17]]
regressor_OLS=sm.OLS(endog=y,exog=Xopt).fit()
regressor_OLS.summary()




plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title('slary vs experiencce')
plt.xlabel('years of experience')
plt.ylabel('salary')
plt.show()