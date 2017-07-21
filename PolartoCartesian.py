# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""



import cv2
import os
import math
from skimage import io
from skimage import img_as_ubyte
import numpy as np

def process_image(dir_Path,new_root):
    
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            #print old_path
            im=cv2.imread(old_path)
            #插入处理函数
            mat=im[:,:,0]
            m=mat.shape[0]
            n=mat.shape[1]
            newmat=np.zeros([2*m-1,2*m-1],dtype=int)
            for i in range(m):
                for j in range(n):
                    r=i
                    theta=2*(math.pi)/n*j 
                    newmat[m-1+int(round(r*math.sin(theta+math.pi/2))),m-1-int(round(r*math.cos(theta+math.pi/2)))]=mat[i,j]
                    newmat=img_as_ubyte(newmat)
            #插入处理函数
                new_name='new'+fileobj
                new_path=os.path.join(new_root,new_name)
                cv2.imwrite(new_path,newmat)
    
#process_image('D:/propig/newpropig5/','D:/propig/newmergepig5/')
'''
im=cv2.imread('D:/TrainingData/0001.png')
mat=im[:,:,0]


m=mat.shape[0]
n=mat.shape[1]
newmat=np.zeros([2*m-1,2*m-1],dtype=int)
for i in range(m):
    for j in range(n):
        r=i
        theta=2*(math.pi)/n*j
        newmat[m-1+int(round(r*math.cos(theta))),m-1+int(round(r*math.sin(theta)))]=mat[i,j]
newmat=img_as_ubyte(newmat)
cv2.imshow('newimg',newmat)
cv2.waitKey(0)
'''

'''def PolartoCartesian(root):
    im=cv2.imread(root)
    mat=im[0]
'''

process_image('D:/TrainingData/TrainingData/ImageData/','D:/TrainingData/TrainingData/PolarImage/')