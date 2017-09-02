# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""

import cv2
import os
import numpy as np

def process_image(dir_Path1,dir_Path2,dir_Path3,dir_Path4):
    res=[]

    tempres1=[]
    tempres2=[]
    tempres3=[]
    for root,dirs,files in os.walk(dir_Path1):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            im=cv2.imread(old_path)
            tempres1.append(im)
    for root,dirs,files in os.walk(dir_Path2):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            im=cv2.imread(old_path)
            tempres2.append(im)
    
    for root,dirs,files in os.walk(dir_Path3):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            im=cv2.imread(old_path)
            tempres3.append(im)
    
    
    for root,dirs,files in os.walk(dir_Path4):
        k=0
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            #print old_path
            im1=tempres1[k]
            im2=tempres2[k]
            im3=tempres3[k]
            im1=np.array(im1,dtype=int)
            im2=np.array(im2,dtype=int)
            im3=np.array(im3,dtype=int)
            k=k+1
            im=cv2.imread(old_path)
            im=im[1:,:,:]
            im=np.array(im,dtype=int)
            
            
            im=im+im1+im2+im3
            
            newim=im[:,:,0]
            newim[newim<765]=0
            newim[newim>=765]=1
            a=np.sum(newim,axis=0)
            
            b=np.where(a>=130)  #a
            
            
            if(len(b[0])==0):
                 
                res.append([fileobj,0])
                continue
            c=[]
            c.append(fileobj)
            c.append(1)
            c.append(b[0][0]+1)
            for i in range(1,len(b[0])):
                #若列序号相差10以内，则视为连续；反之断开，生成新区间
                if b[0][i-1]+1==b[0][i]:
                    continue
                elif b[0][i]-b[0][i-1]>120:#internal 
                    c.append(b[0][i-1]+1)
                    c.append(b[0][i]+1)
            c.append(b[0][-1]+1)
            res.append(c)
           
    #删除区间长度小于5的区间
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
    
'''
    for i in range(len(res)):
        sum=0
        for j in range(2,len(res[i]),2):
            sum=sum+res[i][j+1]-res[i][j]+1
        if sum>90:
            res[i]=[res[i][0],0]
 '''  
        
            
            
if __name__=='__main__':
    result=process_image('D:/TrainingData/Polar_augmentation62000/','D:/TrainingData/Polar_augmentation58800/','D:/TrainingData/Polar_augmentation28400/','D:/TrainingData/polar36800/')
    
    newresult=[]
    for i in result:
        he=0
        if i[1]==1:
            j=3
            while j<len(i):
                he=he+i[j]-i[j-1]
                j=j+2
            if he>140:    #sum
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
    
    
    f=open('a_130_sum_140_intenal_120_uniform_blending_4model_result2.txt','w')
    for word in pre:
        word=str(word)
        f.write(word)
    f.close()
