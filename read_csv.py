#-*-coding:utf-8-*- 
__author__ = 'guojunfeng'
from numpy import *
import pandas as pd
import os
import sys
reload (sys)
sys.setdefaultencoding ('utf-8')
initial_file = 'train'
save_path='distribute'
def read_distributed_csv():
    file_list=os.listdir('train')
    for i in range(len(file_list)):
        df=pd.read_csv(initial_file+'//'+file_list[i])
        save_file='test'+str(i)+'.csv'
        df.to_csv(save_path+'//'+save_file,index=False)


read_distributed_csv()