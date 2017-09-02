# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:38:36 2017

@author: Administrator
"""
import os
import cv2
from skimage.transform import rotate
from skimage import img_as_ubyte

'''
seq = iaa.Sequential([
    #iaa.Crop(px=(0, 16)), # crop images from each side by 0 to 16px (randomly chosen)
    #iaa.Flipud(1.0), # horizontally flip 50% of the images
    iaa.Affine(rotate=90,mode='edge')
    #iaa.GaussianBlur(sigma=(0, 3.0)) # blur images with a sigma of 0 to 3.0
])

img=cv2.imread('D:/TrainingData/TrainingData/TrainingImage/new0001.png')
'''
#newimg=seq.augment_images(img)

'''
newimg=rotate(img,90)
newimg[newimg>0]=1
newimg=img_as_ubyte(newimg)
newimg[newimg>0]=1
'''



def flip_image(dir_Path,new_root):
    
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            #print old_path
            img=cv2.imread(old_path)
            processim=cv2.flip(img,0)
            #processim=cv2.flip(img,1)
            
            new_name=fileobj
            new_path=os.path.join(new_root,new_name)
            cv2.imwrite(new_path,processim)

def rotate_image(dir_Path,new_root):
    if not os.path.exists(new_root):
        os.mkdir(new_root)
    for root,dirs,files in os.walk(dir_Path):
        for fileobj in files:
            old_path=os.path.join(root,fileobj)
            #print old_path
            img=cv2.imread(old_path)
            processim=rotate(img,315)
            #processim[processim>0]=1
            processim=img_as_ubyte(processim)
            #processim[processim>0]=1
            new_name='rt315'+fileobj
            new_path=os.path.join(new_root,new_name)
            cv2.imwrite(new_path,processim)

if __name__=='__main__':
    rotate_image('D:/TrainingData/TrainingData/Polar_TrainingLabel_800/','D:/TrainingData/TrainingData/ImageAugmentation/rotate315/TrainingLabel/')
    #flip_image('D:/TrainingData/TrainingData/wrong_label_image/','D:/TrainingData/TrainingData/ImageAugmentation/horizon_wrong_label/')


