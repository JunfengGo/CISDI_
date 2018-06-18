#-*-coding:utf-8-*- 
__author__ = 'guojunfeng'
from __future__ import division
from numpy import *
import pandas as pd
import tensorflow as tf
import tflearn
import nlp2 as np
#from __future__ import division
from sklearn.model_selection import train_test_split
def calculate_accuracy(a):
    sum_1=0
    total=0
    for i in range(len(a)):
        if label_data[argsort(-a[i])[0]]==1:
            sum_1+=1
            total+=1
        else:
            total+=1
    return sum_1/total
num_mat,categories_mat,label_data,combine_mat=np.process_data()
x_train,x_test,y_train,y_test=train_test_split(combine_mat,label_data,test_size=0.2,random_state=42)
tf.app.flags.DEFINE_integer('epochs',10,'Training epochs')
FLAGS=tf.app.flags.FLAGS
n_features = combine_mat.shape[1]
input = tflearn.input_data ([None, n_features])
network = tflearn.layers.fully_connected (input, 2000, activation='relu')
network = tflearn.dropout(network, 0.5)
network = tflearn.layers.fully_connected (network, 2000, activation='relu')
net = tflearn.dropout(network, 0.5)
y_pred = tflearn.layers.fully_connected (network, 4, activation='softmax')
net = tflearn.regression (y_pred,optimizer='adam',loss='categorical_crossentropy')
model = tflearn.DNN (net)
model.fit (x_train, y_train, validation_set=0.1, n_epoch=FLAGS.epochs)
#metric = model.evaluate (x_test, y_test)
prdict_y=model.predict(x_test)
#test
a=array(prdict_y)
print calculate_accuracy()



