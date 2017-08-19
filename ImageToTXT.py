# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""

import cv2
import os
import numpy as np

def process_image(dir_Path):
    res=[]
    
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            #print old_path
            im=cv2.imread(old_path)
            a=np.sum(im[:,:,0],axis=0)
            a=a/255
            b=np.where(a>=200)
            if(len(b[0])==0):
                
                res.append([fileobj,0])
                continue
            c=[]
            c.append(fileobj)
            c.append(1)
            c.append(b[0][0]+1)
            for i in range(1,len(b[0])):
                if b[0][i-1]+1==b[0][i]:
                    continue
                elif b[0][i]-b[0][i-1]>10:
                    c.append(b[0][i-1]+1)
                    c.append(b[0][i]+1)
            c.append(b[0][-1]+1)
            res.append(c)
    for i in res:
        d=[]
        for j in range(2,len(i),2):
            if(i[j+1]-i[j]<5):
               d.append(j)
               d.append(j+1)
        s=0
        for k in d:
            del(i[k-s])
            s=s+1
    return res
            
            
if __name__=='__main__':
    result=process_image('D:/TrainingData/1200train1/1200testPolar/')
    
    newresult=[]
    for i in result:
        he=0
        if i[1]==1:
            j=3
            while j<len(i):
                he=he+i[j]-i[j-1]
                j=j+2
            if he>140:
                newresult.append(i)
            else:
                i=i[:2]
                i[1]=0
                newresult.append(i)
        else:
            newresult.append(i)
    for i in newresult:
        i[0]=i[0].lstrip('new')
    for i in newresult:
        i.append('\n')
    for i in newresult:
        temp=[x for x in range(1,len(i)) if x%2==0 and x!=len(i)-1]
        temp.insert(0,1)
        k=0
        for j in temp:
            i.insert(j+k,', ')
            k=k+1
        temp1=[x for x in range(5,len(i),3) if x!=len(i)-1]
        k=0
        for j in temp1:
            i.insert(j+k,'  ')
            k=k+1
            
    pre=[x for j in newresult for x in j]
    
    
    f=open('1200_train_result.txt','w')
    for word in pre:
        word=str(word)
        f.write(word)
    f.close()
    
        
    

