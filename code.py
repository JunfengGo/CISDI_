#-*-coding:utf-8-*- 
__author__ = 'guojunfeng'
from numpy import *
import pandas as pd
import sys
import codecs
import os
reload (sys)
sys.setdefaultencoding ('utf-8')



def ReadFile(filePath, encoding):
    with codecs.open (filePath, "r", encoding) as f:
        return f.read ()


def WriteFile(filePath, u, encoding):
    with codecs.open (filePath, "w", encoding) as f:
        f.write (u)




def GBK_2_UTF8(src, dst):
    content = ReadFile (src, encoding='gb18030')
    WriteFile (dst, content, encoding='utf_8')

def change():
 file_list=os.listdir('distribute')
 for i in range(len(file_list)):
     src = 'distribute'+'//'+file_list[i]
     dst = 'change_csv//test'+str(i)+'.csv'
     GBK_2_UTF8 (src, dst)
change()