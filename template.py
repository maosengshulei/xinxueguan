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
def process_image(dir_Path,new_root):
    
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            #print old_path
            im=cv2.imread(old_path,cv2.IMREAD_UNCHANGED)
            im=np.array(im)
            #插入处理函数
            m=im.shape[0]
            n=im.shape[1]
            processim=np.zeros([m,n,3],dtype=int)
            for i in range(3):
                processim[:,:,i]=im;
            processim=img_as_ubyte(processim)
            #插入处理函数
            new_name=fileobj
            new_path=os.path.join(new_root,new_name)
            cv2.imwrite(new_path,processim)
    
process_image('D:/TrainingData/TrainingData/PolarImage/','D:/TrainingData/TrainingData/TrainingImage/')