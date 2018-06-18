#-*-coding:utf-8-*- 
__author__ = 'guojunfeng'
from numpy import *
import pandas as pd
import sys
import os
reload (sys)
sys.setdefaultencoding ('utf-8')
def read_csv():
    label=[]
    filelist=os.listdir('/Users/guojunfeng/Desktop/very/label')
    for i in range(len(filelist)):
        p=pd.read_csv('/Users/guojunfeng/Desktop/very/label'+'/'+'test'+str(i)+'.csv',sep='delimiter', header=None,engine='python'
)
        p=p[0]
        s=0
        for line in p:
            if line==3:
                s+=1
        label.append(s)
    data_label = pd.DataFrame (array (label))
    data_label.to_csv ('/Users/guojunfeng/Desktop/very/new/sss.csv', encoding='utf-8', index=False)


read_csv()