import pandas as pd
import os
def joined():
 initialFile='train'
 save_path='joined_csv'
 save_file='train.csv'
 #os.chdir(initialFile)
 file_list=os.listdir(initialFile)
 df=pd.read_csv(initialFile+'//'+file_list[0])
 #df=df.strip(',')
 df.to_csv (save_path+ '//' + save_file, index=False)
 for i in range(1,len(file_list)):
   df=pd.read_csv(initialFile+'//'+file_list[i])
   #df=df.strip(',')
   df.to_csv(save_path+'//'+save_file,index=False,mode='a+',header=True)
joined()

