#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 18:17:58 2018

@author: aditya
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')

X= dataset.iloc[:,1:2].values  # select columns between 1 & 2 (2 is not included)
y= dataset.iloc[:,2].values     # select column 2

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X,y)  #performed linear regression in X & y

y_pred = regressor.predict(10)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=7)
x_poly=poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)

plt.scatter(X,y,color='red')
plt.plot(X,lin_reg_2.predict(x_poly),color='blue')
plt.title('position salaries')
plt.xlabel('position')
plt.ylabel('salaries')
plt.show()

L = lin_reg_2.predict(x_poly)