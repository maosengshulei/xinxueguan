# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""

import cv2
import math
import os
import numpy as np
from skimage import io
from skimage import img_as_ubyte


def process_image(dir_Path,new_root):
    
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            #print old_path
            im=cv2.imread(old_path)
            height,width,channel=im.shape
            processim=np.zeros([height/2,720,channel],dtype=int)
            height=int(height)
            width=int(width)
            channel=int(channel)
            for i in range(height):
                for j in range(width):
                    magnitude,angle=cv2.cartToPolar(j-351,height-1-i-351)
                    mag=int(round(magnitude[0][0]))
                    if mag>351:
                        continue
                    ang=(90+angle[0][0]*180/math.pi)%360
                    ang=int(round(ang*2))
                    processim[mag-1,ang-1,:]=im[i,j,0]
                        
            processim=img_as_ubyte(processim)
            #插入处理函数
            new_name=fileobj
            new_path=os.path.join(new_root,new_name)
            cv2.imwrite(new_path,processim)

if __name__=='__main__':
    process_image('D:/TrainingData/test400_addblack/test400_addblack/','D:/TrainingData/test400_addblack/test/')
    '''
    im=cv2.imread('D:/TrainingData/1000train/1000train/new0005.png')
    height,width,channel=im.shape
    
    processim=np.zeros([height/2,720,channel],dtype=int)
    height=int(height)
    width=int(width)
    channel=int(channel)
    for i in range(height):
        for j in range(width):
            magnitude,angle=cv2.cartToPolar(j-351,height-1-i-351)
            
            
            mag=int(round(magnitude[0][0]))
            if(mag>351):
                continue
            ang=(90+angle[0][0]*180/math.pi)%360
            ang=int(round(ang*2))
            processim[mag-1,ang-1,:]=im[i,j,0]
    processim=img_as_ubyte(processim)
    cv2.imwrite('test1.png',processim)
    '''