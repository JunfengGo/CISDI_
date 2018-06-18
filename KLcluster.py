# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 19:03:50 2018

@author: hasee
"""

import time    
from sklearn import metrics    
import pickle as pickle    
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy import optimize as opt
#import system
#sys.setdefaultencoding('utf-8')

#数据处理
filename= "Ex0.csv"
Steeldata = pd.read_csv(filename)
SD=Steeldata[Steeldata.STAND_NO == 7]
SD=SD.dropna()
SD=SD.drop(['STAND_NO','kmAct','STRIP_NO','KM','STRAIN_RATE'],axis = 1 )
#横纵坐标
STRAINP = SD['STRAINRATE_POST']
SD.drop(labels=['STRAINRATE_POST'],axis=1,inplace = True)
SD.insert(0,'STRAINRATE_POST',STRAINP)
x=SD.STRAINRATE_POST

#%%

#线聚类算法

#聚类线
def funcline(x,c,m):
        return c*(x**m)
#随机初始化k条曲线(即随机初始c，m)
def intiCMk(k):
    cm = zeros((k, 2))
    for i in range(k):
        cm[i,:]=[random.uniform(175,300),random.uniform(0,0.01)]
    print('cm=',cm)
    return cm

#计算点v1到曲线的距离
def D_F(v1,v2):
# ——————————————————计算点到曲线的距离的平方函数
    points=[]
    def DLD_func(p):
        
        #v1=[75,200]
        #v2=[230.87,0.0033]
        [s,t] = [v1[0,0],v1[0,1]]
        [c,m] = [v2[0],v2[1]]
        x=p
        y=c*(x**m)
        z=(x-s)**2 + (y-t)**2  #距离
        points.append((x,z))
        return z
    #计算最短距离 即真正的点到曲线的距离
    init_point=40
    
    result=opt.fmin(DLD_func,init_point,full_output=True)
    
    
    minDLD = result[1]
    return minDLD
#————————————————曲线拟合函数
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def NH(dataSet,numpoint):
    #x=data.STRAINRATE_POST
    #y=data.kmCal
    x=[]
    y=[]
    x1=dataSet[:,0]
    y1=dataSet[:,1]
    #numSamples=6000
    
    for i in range(numpoint):
        x.append(x1[i,0])
        y.append(y1[i,0])
    def funcline(x,c,m):
        return c*(x**m)

    popt, pcov = curve_fit(funcline, x, y)
    c=popt[0]         #popt里面是拟合系数
    m=popt[1]
    
    v2=[]
    v2.append(c)
    v2.append(m)
    #print (v2)
    return v2

#%%
    
#——————————依据曲线进行聚类的线聚类函数
def Lcluster(dataSet,k):
    numSamples = dataSet.shape[0] 
    #第一栏储存分类标签
    #第二栏储存距离
    clusterAssment = mat(zeros((numSamples, 2)))  
    clusterChanged = True
    
    ##第一步初始化k条曲线，k组c,m向量v2
    #v2 = intiCMk(k)
    
    v2 = np.array([[75,0.24],[80,0.24],[100,0.24],[110,0.24]])
    print(v2)
    #for i in range(k):  
        #plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12) 
        
        #xx=np.arange(x.min(),x.max(),1)
        #vv=v2[i]
        #yvals=funcline(xx,vv[0],vv[1])
        #plt.plot(xx, yvals, 'm',label='curve_init values')
        #plt.axis([0, 200, 100,350 ]) 
        #·plt.legend(loc=1)
        
    
    Internum=1
    while clusterChanged:  
        Internum=1+Internum
        clusterChanged = False  
        ## 对每个样本 ,把每个样本点划分到离它最近的中心点 
        for i in range(numSamples):  
            minDist  = 100000.0  
            minIndex = 0  
            ##第二步:计算到两条曲线的距离
            for j in range(k):
                distance = D_F(dataSet[i,:], v2[j])
                #print(distance)
                if distance < minDist:
                    minDist = distance
                    minIndex = j        #如果第i个数据点到第j个中心点更近，则将i归属为j 
                    #print(minIndex)
            ##第三步：更新分类标签
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist**2       #并将i个数据点的分配情况存入字典  
                #print('____________*_____________')
                #print(clusterAssment)
        
        ##第四步：更新聚类曲线，采用重新在簇内拟合的方式
       
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]  #取第一列等于j的所有行
            numpoint = pointsInCluster.shape[0]
            #print('*********************')
            #print(pointsInCluster)
            #print('v2=',v2[j,:])
            #print('numpoint=',numpoint)
            v2[j,:] = NH(pointsInCluster, numpoint)
    print ('Congratulations, cluster complete!')  
    return v2, clusterAssment, Internum

#%%
#可视化函数
def showCluster(dataSet, k, v2, clusterAssment):  
    numSamples, dim = dataSet.shape  
    if dim != 2:  
        print ("Sorry! I can not draw because the dimension of your data is not 2!")  
        return 1  
  
    #mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    mark = ['r.','bx','gd','k+']
    if k > len(mark):  
        print ("Sorry! Your k is too large! please contact Zouxy")  
        return 1  
    
    #plt.figure(figsize=(15,10))  
    # 画出所有点

    fig = plt.figure(figsize=(15,10))
    ax = fig.add_subplot(111) 
    for i in range(numSamples):  
        markIndex = int(clusterAssment[i, 0])
        ax.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex],markersize=15)  
       #ax.scatter(dataSet[i, 0], dataSet[i, 1], s=50, color='dimgray',marker=mark[markIndex])
    #markl = ['black', 'red', 'orange', 'lawngreen', 'skyblue', 'midnightblue', 'blueviolet', 'm', 'crimson', 'lightpink']  
    # 画出k条聚类线 
    linestyle = ['-', '--', '-.', ':']
    color = ['black', 'red', 'orange', 'lawngreen', 'skyblue', 'midnightblue', 'blueviolet']
    for i in range(k):  
        #plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12) 
        
        xx=np.arange(x.min(),x.max(),1)
        vv=v2[i]
        yvals=funcline(xx,vv[0],vv[1])
        label='cluster_line'+str(i)
        #plt.figure(figsize=(15,10))
        ax.plot(xx, yvals, linestyle=linestyle[i], color=color[i], label=label)
    plt.legend(loc='best')
    plt.ylim ((0, 1000))
    my_y_ticks = np.arange (0, 1000, 200)
    plt.yticks (my_y_ticks)
    plt.xlabel ("变形速率/s", fontproperties='SimHei', size=20)
    plt.ylabel ("变形抗力/MPa", fontproperties='SimHei', size=5)
    plt.show()
    plt.savefig(r'C:\Users\hasee\Desktop\图\聚类图.png')
    #plt,title('')

#%%
#主程序
from numpy import *  
import time  
import matplotlib.pyplot as plt  
  
## step 1: load data  
print ("step 1: load data...")  
dataSet = SD  

  
## step 2: clustering...  
print ("step 2: clustering..." ) 
dataSet = mat(dataSet)  
k = 3
v2, clusterAssment ,Internum= Lcluster(dataSet, k)  
#%%
## step 3: show the result  
print ("step 3: show the result...")  
showCluster(dataSet, k, v2, clusterAssment)  

print(Internum)
print(v2)