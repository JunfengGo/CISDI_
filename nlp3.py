from __future__ import division
#-*-coding:utf-8-*-
__author__ = 'guojunfeng'
#from __future__ import division
from numpy import *
import re
import pandas as pd
import os
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
#label=[]
def combine_disable(train_data):
    c=0
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
    #for i in range(len(key)):
        #l1.append(key[i])
    return l1

def process_data(train_data,label):
    label1=[]
    #label = zeros ((len (train_data), 4))
    #num_mat = zeros ((len (train_data), 4))
    for i in range(len(train_data)):
        #label=get_outcome (train_data[i], i)
        #w,x,y,z,key_dict=get_label(train_data[i])
        #get_outcome(train_data[i],label)
        list,sum_cha=get_label(train_data[i])
        #print list
        g=check_water(sum_cha,list)
        label1.append(g)
    data_2 = pd.DataFrame (array (label1))
    #print index
    data_2.to_csv ('/Users/guojunfeng/Desktop/very/continue' + '/'+str(1111111111)+'.csv', encoding='utf-8', index=False)
        #num_mat[i][0]=int(w)
        #num_mat[i][1] = int(x)
        #num_mat[i][2] =int( y)
        #num_mat[i][3] = int(z)
    #categories_mat = zeros ((len (train_data), len(key)))
    #for i in range(len(train_data)):
        #w,x,y,z,key_dict=get_label(train_data[i])
        #categories_mat = zeros ((len (train_data2), 801))
        #for item in key_dict:
            #index_num = key.index(item[0])
            #categories_mat[i][index_num] = int(item[1])

    #savetxt('new2.csv',mat(hstack((num_mat,categories_mat))),delimiter=',')
    #data_1=pd.DataFrame(num_mat,columns=make_col())
    #data_1.to_csv('outcome'+'//'+file_list,encoding='utf-8',index=False)
    #data_label=pd.DataFrame(array(label))
    #data_label.to_csv('label'+'//'+file_list,encoding='utf-8',index=False)
    #print label
    #data_2=pd.DataFrame(array(label1))
    #print label1
    #data_2.to_csv('/Users/guojunfeng/Desktop/very/continue'+'file.csv',encoding='utf-8',index=False)
    #return label.count(3)
    #return mat(num_mat),mat(categories_mat),mat(hstack((num_mat,categories_mat)))
def get_outcome(line,label):
    #label = zeros ((len (train_data2), 4))
    #label=[]
   # h=0
    line_block=line.split(',')
    #if line_block[0].isdigit():
      #h=int(line_block[0])-1
      #label[i][h]=1
    #else:
      #label[i][h]=label[i-1][h]
    label.append(line_block[0])
    #return label
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
    #return count_feature(list)
    return list,count_feature(list)
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
    return sum_cha
    #int(sum_eng),int(sum_cha),int(sum_num),int(sum_sym),c
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
        #list.append(item.strip(' '))
        if item!='':
            item.strip(' ')
            list.append(item)
    return list
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def check_water(sum_cha,line):
    #conti_index=1
    label_index=[]
    #line_block=line.split(',')
    for item in line:
        if is_number(item):
            label_index.append(line.index(item))
            line[line.index(item)]=float(item)+0.0012345*0.12323
    #!print label_index
    g=get_continue(label_index)
    #print g
    #print sum_cha,len(line)
    return [g/len(line),sum_cha/len(line)]
def get_continue(line):
    sum1=0
    label_all=[]
    x=0
    recur(line,x,label_all)
    for item in label_all:
        if len(item)>sum1:
            sum1=len(item)
    #print sum1recur
    #print sum1
    return sum1
    #print sum1
def recur(line,x,label_all):
    if len(line)==0:
        label_all=['']
    else:
        label=[x]
        index_end=x
        for i in range(x+1,len(line)):
            if line[i]-line[x]==i-x:
                label.append(i)
                index_end=i
        label_all.append(label)
        if index_end!=len(line)-1:
            recur(line,index_end+1,label_all)
def read_allcsv():
  #label_num=[]
  #label_num=[]
  #file_list=os.listdir('change_csv')
  #for i in range(len(file_list)):

     #train_data=pd.read_csv('change_csv'+'//'+'test'+str(i)+'.csv',sep='delimiter', header=None,engine='python')
     #sep='delimiter', header=None,engine='python')
     #train_data=train_data[0]
   label_num = []
   label = []
   train_data=pd.read_csv('/Users/guojunfeng/Desktop/very/joined_csv/gg.csv',sep='delimiter', header=None,engine='python')
   train_data=train_data[0]
   train_data=combine_disable(train_data)
   label_num1=process_data(train_data,label)
   label_num.append(label_num1)
     #label_num.append(label.count('3'))
#label=zeros((len(train_data2),4))
#num_mat=zeros((len(train_data),4))
  #label1=pd.DataFrame(array(label_num))
  #label1.to_csv('/Users/guojunfeng/Desktop/very/new'+'/'+'yyyyyyyyyy',encoding='utf-8',index=False)
key=[]
read_allcsv()
#categories_mat=zeros((len(train_data2),801))
#p=train_data2
#print