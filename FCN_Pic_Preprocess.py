# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""

import cv2
import os
import math
import xinxueguan
import numpy as np
from skimage import io
from skimage import img_as_ubyte
import matplotlib.pyplot as plt  

'''
label_list=xinxueguan.labellist('D:\TrainingData\TrainingData\label.txt')



l1=label_list[0]
'''
def get_angle(label_list):
    templist=[]
    newlabellist=[]
    if(label_list[1]=='0'):
        return []
    else:
        templist=label_list[2:]
        if(int(templist[0])==1 and int(templist[-1])==720):
            templist[0]=0
        for i in templist:
            newlabellist.append(int(i)/2)
        return newlabellist

def get_ordinate(label_list):
    templist=[]
    if(label_list[1]=='0'):
        return []
    else:
        templist=label_list[2:]
        if(int(templist[0])==1 and int(templist[-1])==720):
            if(len(templist)>2):
                del templist[0]
                a=templist.pop(0)
                del templist[-1]
                b=templist.pop(-1)
                templist.insert(0,a)
                templist.insert(0,b)
        l=len(templist)
        for i in range(l):
            r=351
            theta=2*(math.pi)/720.0*(int(templist[i])-1)
            templist[i]=[r+int(round(r*math.sin(theta+math.pi/2))),r-int(round(r*math.cos(theta+math.pi/2)))]
            
        return templist


def label_image(dir_Path,new_root,labellist):
    k=1000
    
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            im=cv2.imread(old_path)
            llist=labellist[k]
            nlabel=get_angle(llist)
            m=im.shape[0]
            n=im.shape[1]
            newimg=np.zeros([m,n],dtype=int)
            newimg=img_as_ubyte(newimg)
            if(len(nlabel)!=0):
                j=0
                while(j<len(nlabel)):
                    a=nlabel[j]
                    j=j+1
                    b=nlabel[j]
                    j=j+1
                    cv2.ellipse(newimg,(351,351),(351,351),90,-b,-a,1,-1)
                
            new_name='label'+fileobj
            new_path=os.path.join(new_root,new_name)
            cv2.imwrite(new_path,newimg)
            k=k+1
'''
nl1=get_angle(l1)

print nl1

img1=cv2.imread('D:/TrainingData/TrainingData/PolarImage/new0001.png')

m=img1.shape[0]
n=img1.shape[1]
newimg1=np.zeros((m,n),dtype=int)


newimg1=img_as_ubyte(newimg1)

i=0
while(i<len(nl1)):
    
    a=nl1[i]
    i=i+1
    b=nl1[i]
    i=i+1
    cv2.ellipse(newimg1,(351,351),(351,351),90,-b,-a,1,-1)
plt.imshow(newimg1, cmap = 'gray')
cv2.imwrite('test1.png',newimg1)
'''
if __name__=='__main__':
    label_list=xinxueguan.labellist('D:\TrainingData\TrainingData\label.txt')
    label_image('D:/TrainingData/TrainingData/PolarImage2/','D:/TrainingData/TrainingData/LabelImage/',label_list)
    
