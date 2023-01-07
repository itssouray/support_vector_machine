# -*- coding: utf-8 -*-
"""Support Vector machine classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pa71i4tEpzmZCue0gnFIKnPisP4Gc_68
"""

import numpy as np

class svm_classifier :

  #initiating the hyperparameters
  def __init__(self,learning_rate,no_of_iteration,lambda_parameter):
    self.learning_rate = learning_rate
    self.no_of_iteration = no_of_iteration
    self.lambda_parameter = lambda_parameter



  #fitting the dataset for svm classifier
  def fit(self,X,Y):
    self.m, self.n = X.shape

    self.w = np.zeros(self.n)
    self.b = 0

    self.X = X
    self.Y = Y

    for i in range(self.no_of_iteration):
      self.update_weight()



  #updating the value of weight and bias for minimum loss function 
  def update_weight(self):

    # converting value of y (which is 0 and 1) into -1 and 1
    # if y<0 --> y = -1
    # if y>0 --> y = 1
    y_label = np.where(self.Y <=0, -1, 1)

    for index , x_i in enumerate(self.x):
      
      # if (y.(wx+b)>=1) then --> ( dw = 2 * lambda*w) and (db = 0)
      # else if (y.(wx+b)<1) then --> ( dw = 2 * lambda*w - x.y) and (db = y)
      condition = y_label[index]*(np.dot(x_i,self.w) - self.b) >= 1

      if (condition == True):
        dw = 2 * self.lambda_parameter*self.w
        db = 0

      else:
        dw = 2 * self.lambda_parameter*self.w - np.dot(x_i,y_label[index])
        db = y_label[index]

      self.w = self.w - self.learning_rate*dw
      self.b = self.b - self.learning_rate*db



  
  def predict(self,X):
    output = np.dot(X,self.w) - self.b

    # converting output value into positive or negative val i.e  1 or -1
    predicted_label = np.sign(output)

    # if value is -1 assign 0 else if 1 assign 1
    y_hat = np.where(predicted_label <=-1 ,0,1)

    return y_hat

model = svm_classifier(learning_rate=0.001,no_of_iteration=1000,lambda_parameter=0.01)

