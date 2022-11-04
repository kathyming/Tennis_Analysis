#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 17:36:34 2021

@author: FouadZ
""" ####      NOMINAL LOGISTIC REGRESSION

# Multiple Categories in no logical order

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression

# Open file
df = pd.read_csv('glass.csv')


#Make model and split
nom_regr = linear_model.LogisticRegression(multi_class = 'multinomial', solver='newton-cg').fit(x_train,y_train)                                                                         

x_train, x_test, y_train, y_test = train_test_split(df.drop('Type',axis=1), df['Type'], test_size=0.25)

# Make prediction
y_pred = nom_regr.predict(x_test)

print(confusion_matrix(y_test,y_pred))

# Actual values in rows
# Predcited Values in columns

print(classification_report(y_test,y_pred))
                                                                               