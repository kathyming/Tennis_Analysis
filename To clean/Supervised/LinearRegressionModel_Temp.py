#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:35:55 2021

@author: FouadZ
"""
#       Linear Regression   # Response = Continuous Data (Can have decimals)


import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import linear_model

# Open File
df = pd.read_csv('mult_regr.csv')

# Split the data
x_train, x_test, y_train, y_test = train_test_split(df.drop('HeatFlux',axis=1), df['HeatFlux'], test_size=0.25)
# X is predictors Y is response

# Create Model
linear_regr = linear_model.LinearRegression()
linear_regr.fit(x_train, y_train)

# Make Prediction
y_pred = linear_regr.predict(x_test)

# Residuals && Sum of SOR

# Sum of squares of residuals
# Difference between actual value and predicted value = Residual
# This sum should ideally be as close to 0 as possible.
residual = []
for ctr in range(len(list(y_pred))):
    resid = list(y_pred)[ctr] - list(y_test)[ctr]
    residual.append(resid**2)
    
SOR = sum(residual)