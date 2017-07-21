# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""

import cv2
import os
from skimage import io
from skimage import img_as_ubyte

def process_image(dir_Path,new_root):
    
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            #print old_path
            im=io.imread(old_path)
            #插入处理函数
            processim=img_as_ubyte(im)
            #插入处理函数
            new_name='newpro'+fileobj
            new_path=os.path.join(new_root,new_name)
            io.imsave(new_path,processim)
    
process_image('D:/propig/propropig/propropig5/','D:/propig/unit8pig/pig5/')
