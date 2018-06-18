#-*-coding:utf-8-*- 
__author__ = 'guojunfeng'
from numpy import *
import re
import pandas as pd
from collections import Counter
#train_data=pd.read_csv('joined_csv/gg.csv',sep='delimiter', header=None,engine='python')
#train_data=train_data[0]
#label=zeros((len(train_data),4))
#num_mat=zeros((len(train_data),4))
#key=[]
#categories_mat=zeros((len(train_data),801))
#mat_test=zeros((len(p),))
#a=train_data[0].split(',')
#for item in a:
   # if 'Unnamed' in item:
        #a.remove(item)
#b=a[1].decode('UTF-8')
#print b
#ub=unicode(b)
#print ub
#v=re.findall(ur'[\u4e00-\u9fff]+',ub)
#v1=v[0].encode('UTF-8')
#v1=v1.decode('UTF-8')
#print len(v1)
#v2=re.findall(ur'[\u0041-\u005a]',ub)
#v3=v2[0].encode('UTF-8')
#v4=v3.decode('UTF-8')
#print len(v)
#d=train_data
def combine_disable():
    for i in range (len (train_data)):
        if train_data[i][0].isdigit ():
            c = i
        else:
            train_data[c] = train_data[c] + train_data[i]
            train_data[i] = ''
    d=train_data
    for i in range(len(train_data)):
        if train_data[i]=='':
            d=d.drop(i)
    d.index=range(len(d))
    return d
def make_col():
    l1=['english','cha','num','symbol']
    for i in range(len(key)):
        l1.append(key[i])
    return l1

def process_data(train_data):
    label = zeros ((len (train_data), 4))
    num_mat = zeros ((len (train_data), 4))
    for i in range(len(train_data)):
        label=get_outcome (train_data[i], i)
        w,x,y,z,key_dict=get_label(train_data[i])
        #get_outcome(train_data[i],i)
        num_mat[i][0]=int(w)
        num_mat[i][1] = int(x)
        num_mat[i][2] =int( y)
        num_mat[i][3] = int(z)
    categories_mat = zeros ((len (train_data), len(key)))
    for i in range(len(train_data)):
        w,x,y,z,key_dict=get_label(train_data[i])
        #categories_mat = zeros ((len (train_data2), 801))
        for item in key_dict:
            index_num = key.index(item[0])
            categories_mat[i][index_num] = int(item[1])

    #savetxt('new2.csv',mat(hstack((num_mat,categories_mat))),delimiter=',')
    data_1=pd.DataFrame(hstack((num_mat,categories_mat)),columns=make_col())
    data_1.to_csv('pd_data.csv',encoding='utf-8')
    return mat(num_mat),mat(categories_mat),mat(label),mat(hstack((num_mat,categories_mat)))
def get_outcome(line,i):
    label = zeros ((len (train_data2), 4))
    h=0
    line_block=line.split(',')
    if line_block[0].isdigit():
      h=int(line_block[0])-1
      label[i][h]=1
    else:
      label[i][h]=label[i-1][h]
    return label
def get_label(line):
   # l=[]
   # line_block=line.split(',')
    #for item in line_block:
        #if 'Unnamed' in item:
            #line_block.remove (item)

    #for item in line_block:
        #if item=='':
            #line_block.remove(item)
    #line_block.remove(line_block[0])
    #for item in line_block:
       # l.append(item.strip(' '))
    list=delete_trush(line)
    return count_feature(list)
def count_feature(line_block):
    sum_cha=0
    sum_num=0
    sum_sym=0
    sum_eng=0
    instant=''
    for item in line_block:
        u=unicode(item,'UTF-8')
        u1=re.findall (ur'[\u4e00-\u9fff]+', u)
        if u1==[]:
            sum_cha+=0
        else:
            for item in u1:
                instant=instant+item
                u2=item.encode('UTF-8')
                u2=u2.decode('UTF-8')
                sum_cha+=len(u2)
    c=Counter(instant)
    c=c.most_common(6)
    for item in c:
        if item[0] in key:
            continue
        else:
            key.append(item[0])
    for item in line_block:
        u=unicode(item,'UTF-8')
        u1=re.findall (ur'[\u0041-\u005a]', u)
        if u1==[]:
            sum_eng+=0
        else:
            for item in u1:
                u2=item.encode('UTF-8')
                u2=u2.decode('UTF-8')
                sum_eng+=len(u2)
    for item in line_block:
        u=unicode(item,'UTF-8')
        u1=re.findall (ur'[\u0061-\u007a]', u)
        if u1==[]:
            sum_eng+=0
        else:
            for item in u1:
                u2=item.encode('UTF-8')
                u2=u2.decode('UTF-8')
                sum_eng+=len(u2)
    for item in line_block:
        u=unicode(item,'UTF-8')
        u1=re.findall (ur'[\u0030-\u0039]', u)
        if u1==[]:
            sum_num+=0
        else:
            for item in u1:
                u2=item.encode('UTF-8')
                u2=u2.decode('UTF-8')
                sum_num+=len(u2)
    for item in line_block:
        u=unicode(item,'UTF-8')
        if u==[]:
            sum_sym+=0
        else:
            for item in u:
                u2=item.encode('UTF-8')
                u2=u2.decode('UTF-8')
                sum_sym+=len(u2)
    sum_sym=sum_sym-sum_num-sum_cha-sum_eng
    return int(sum_eng),int(sum_cha),int(sum_num),int(sum_sym),c
def delete_trush(line):
    list=[]
    l=[]
    sum=1
    line_block=line.split(',')
    for item in line_block:
        if item=='':
            line_block.remove(item)
        if 'Unnamed:' in item:
            l.append(line_block.index(item))
    if len(l)!=0:
        line_block.pop(l[0])
        l.remove(l[0])
        if len(l)!=0:
            for i in l:
                line_block.pop(i-sum)
                sum+=1
    if line_block[0].isdigit():
        line_block.remove(line_block[0])
    for item in line_block:
        list.append(item.strip(' '))
    return list

train_data=pd.read_csv('joined_csv/gg.csv',sep='delimiter', header=None,engine='python')
train_data=train_data[0]
train_data2=combine_disable()
#label=zeros((len(train_data2),4))
#num_mat=zeros((len(train_data),4))
key=[]
#categories_mat=zeros((len(train_data2),801))
p=train_data2
process_data(p[0:60])
#print
