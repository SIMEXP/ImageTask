#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:58:36 2020

@author: francois
"""

import os
import sys
sys.path.append('../')
sys.path.append('../brisque')
print(sys.path)

import cv2
from brisque import BRISQUE
from os.path import basename as bname
from tqdm import tqdm
#from utilities import root_path

brisq = BRISQUE()

def loadimages(impath):
    '''
    Description
    -----------
    Lists the full relative path of all '.jpeg' files in a directory.

    Parameters
    ----------
    imdir: type = str
        Name of the directory containing the images.

    Return
    ------
    imlist: type = list
        1D list containing all '.jpeg' files' full relative paths
    '''
    imlist = []
    for allimages in os.walk(os.path.abspath(impath)):
        for image in allimages[2]:
            if '.jpg' in image:
                imlist.append(os.path.join(allimages[0],image))
    return imlist

def run_analysis():
    imagelist = loadimages('/home/francois/Desktop/neuromod_image_bank/inanimate/bathroom/bathtub')
    names = list()
    feature = list()
    score = list()
    for picpath in tqdm(imagelist):
        names.append(bname(picpath))
        feature.append(brisq.get_feature(picpath))
        score.append(brisq.get_score(picpath))
    qc_dict = {'name':names, 'feature':feature, 'score':score}
    return qc_dict
qc_bathroom = run_analysis()