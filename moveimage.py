# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""

import cv2
import os
import numpy as np
from skimage import io
from skimage import img_as_ubyte

def channel_moveimage(img,k,new_path):
    im=cv2.imread(img,cv2.IMREAD_UNCHANGED)
    im=np.array(im)
    m,n=im.shape
    
    n=n+k
    processim=np.zeros([m,n],dtype=int)
    processim[:,0:k]=im[:,n-2*k:n-k]
    processim[:,k:n+k]=im[:,0:n-k]
    newim=processim[:,0:n-k]    
    newim=img_as_ubyte(newim)
    cv2.imwrite(new_path,newim)
    

def process_image(dir_Path,new_root,k):
    
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            new_name=fileobj
            new_path=os.path.join(new_root,new_name)
            channel_moveimage(old_path,k,new_path)
            
            
            
            
            
def moveimage(img,k,new_path):
    im=cv2.imread(img,cv2.IMREAD_UNCHANGED)
    im=np.array(im)
    m,n=im.shape
    result=np.zeros([m,n,3],dtype=int)
    n=n+k
    processim=np.zeros([m,n,3],dtype=int)
    processim[:,0:k,0]=im[:,n-2*k:n-k]
    processim[:,k:n+k,0]=im[:,0:n-k]
    newim=processim[:,0:n-k,0]
    for i in range(3):
        result[:,:,i]=newim
    
    
    processim=img_as_ubyte(result)
    cv2.imwrite(new_path,result)



#moveimage('D:/TrainingData/TrainingData/ImageData_copy1000/0001.png',30,'D:/TrainingData/TrainingData/Move_trainingdata/0001.png')
    
if __name__=='__main__':   
    process_image('D:/TrainingData/TrainingData/origin_polar_image_label_copy1000/','D:/TrainingData/TrainingData/Move_labeldata/move690/',690)
