#-*-coding:utf-8-*-
import pandas as pd
from numpy import *
import codecs


def ReadFile(filePath, encoding):
    with codecs.open (filePath, "r", encoding) as f:
        return f.read ()


def WriteFile(filePath, u, encoding):
    with codecs.open (filePath, "w", encoding) as f:
        f.write (u)




def GBK_2_UTF8(src, dst):
    content = ReadFile (src, encoding='gb18030')
    WriteFile (dst, content, encoding='utf_8')


src = 'joined_csv/train.csv'
dst = 'joined_csv/qyx_utf8.csv'
GBK_2_UTF8 (src, dst)

#def preprocessing():
  #train_data=pd.read_csv('joined_csv/train.csv',sep='delimiter', header=None,encoding='gb18030',engine='python')
  #n=zeros((len(train_data),3))
  #line=''
  #for i in range(len(train_data)):
      #line=train_data[i].strip('')
#def check_contain_chinese(check_str):
    #sum_cha=0
    #for ch in check_str.decode ('utf-8'):
        #if u'\u4e00' <= ch <= u'\u9fff':
          #  sum+=1
    #return sum_cha
