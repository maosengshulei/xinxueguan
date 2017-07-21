# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""

import cv2
import os

def labellist(file_path):
    #file_path='D:\TrainingData\TrainingData\label.txt'
    with open(file_path) as fileobj:
        lines=fileobj.readlines()

    newlines=[]
    for line in lines:
        line=line.replace(',',' ')
        newline=line.split()
        newlines.append(newline)
    return newlines



def process_image(dir_Path,new_root):
    i=0
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            
            im=cv2.imread(old_path)
            newim=label(im,newlines[i])
            print i
            i=i+1
            new_name='labeled'+fileobj
            new_path=os.path.join(new_root,new_name)
            cv2.imwrite(new_path,newim)

def label(img,line):
    if(line[1]==0):
        return img
    else:
        for i in range(2,len(line)):
            img[:,int(line[i])-1,0]=0
            #img[:,int(line[i]),0]=0
            img[:,int(line[i])-1,1]=0
            #img[:,int(line[i]),1]=0
            img[:,int(line[i])-1,2]=255
            #img[:,int(line[i]),2]=255
        return img

if __name__=='__main__':
    process_image('D:/TrainingData/TrainingData/ImageData/','D:/TrainingData/TrainingData/TestData/')