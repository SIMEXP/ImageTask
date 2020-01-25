#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:37:15 2019

@author: francois
"""
import numpy as np
import nibabel as nib
from nibabel.testing import data_path
#import nilearn
import os
import pandas as pd
from PIL import Image
import warnings
warnings.filterwarnings('ignore')
from nilearn import plotting
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from nilearn.image import mean_img
from nilearn.image import smooth_img

#subj01anat = '/home/francois/haxby_full/haxby2001/subj1/anat.nii.gz'

#from nilearn import datasets
#haxby_ds = datasets.fetch_haxby(data_dir='/home/francois/haxby_full', subjects=(1, 6), fetch_stimuli=True, url=None, resume=True, verbose=1)

#sub1_func = os.path.join(os.getcwd(), 'sub-1_task-objectviewing_run-01_bold.nii.gz')
#image = nib.load(sub1_func)
#image_shape = image.shape
#data_type = image.get_data_dtype()
#header = image.header
#subj = '/home/francois/object_recognition_haxby_ds000105-download/sub-1/func'
#def get_intersubj_mean(subj_func):
#    os.chdir(subj_func)
#    nruns = [os.path.abspath(nrun)
#            for nrun in os.listdir(subj_func)
#            if nrun.endswith('.gz')]
#    for nrun in range(len(nruns)):
#        image = nib.load(nruns[nrun])
#        imshape = image.shape
#        hdrs = image.header
#        print(hdrs)
##        img_data = image.get_data()
def get_anat():
    images = []
    subjs = [os.path.join(os.getcwd(),subj) for subj in os.listdir(os.getcwd()) if 'sub' in subj] 
    for subj in subjs:
        for 'anat' in os.listdir(subj):
            
#        images = [os.path.join(os.getcwd(),subjs[scan.index()],scan) 
#                 for scan in subjs
#                 if 'T1w.nii.gz' in scan]
#        return images
        print(scan)
#                for image in images:
#                    plotting.plot_img(image)
#                    smoothimg = smooth_img(image)
#                    plotting.plot_img(smoothimg)
        
        
#images = [[image for image in allim[2]] for allim in os.walk() ]
        
#        images = [mean_img(nruns[nrun]) for nrun in range(len(nruns))]
#Image.open('testplot.png').save('testplot.jpg','JPEG')
#        for image in images:
#            mean_image = mean_img(image)
#    plotting.plot_img(mean_image)
        
images = get_anat()
#os.listdir('/home/francois/object_recognition_haxby_ds000105-download/sub-1/func')
#image = nib.load('/home/francois/object_recognition_haxby_ds000105-download/sub-1/anat/sub-1_T1w.nii.gz')
#image.dtype=np.float32
## Get data from nibabel image object (returns numpy memmap object)
#img_data = image.get_data()
#
## Convert to numpy ndarray (dtype: uint16)
#img_data_arr = np.asarray(img_data)
#img_data_arr.dtype = np.float32
#img = Image.fromarray(img_data_arr)
#
#plt.imshow(img_data_arr)
#imageseries = pd.Series(image)
#headers = pd.Series(image.header)
#frame = {
#imarray = np.ndarray(image, shape=image.shape, dtype=np.float32)
