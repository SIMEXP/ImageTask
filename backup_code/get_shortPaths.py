# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 01:27:34 2019

@author: Francois
"""

from PIL import Image
import glob
import os
import platform
import pandas as pd
from shutil import move as mv
from tqdm import tqdm
from flatten import flatten

def get_shortPaths(catName,extension='.jpg'):
    cwd = os.getcwd()
    check = platform.system()
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    refs = sources['reference'].tolist()
    altRefs = [ref.upper() for ref in refs]
    references = refs+altRefs
    shortpathlist_toDF = []
    shortpathlist = []
        # Adapting the directory paths to the appropriate OS
    if check == 'Windows':
        catPath = cwd +'\\'+ catName
    else:
    	catPath = cwd +'/'+ catName
    subDirs = [os.path.join(catPath,dirname) 
              for dirname in os.listdir(catPath)]
    for subDir in subDirs:
        print(len(os.listdir(subDir)))
    fPaths = flatten([[os.path.abspath(os.path.join(subDir,filename))
             for filename in os.listdir(subDir)]
             for subDir in subDirs.__iter__()])
#        print(len(fPaths))
    for imPath in fPaths.__iter__():
#        print(imPath)
        for ref in references.__iter__():
#            print(ref)
            refInd = imPath.find(ref)
            if refInd != -1:
#                print(refInd)
                longpath, ext = os.path.splitext(imPath)
                shortpath = longpath[:longpath.find(ref)]+extension
                shortpathlist.append(shortpath)
                shortpathlist_toDF.append((shortpath,imPath))
                mv(imPath,shortpath)
    shortpathlist_toDF = pd.DataFrame(shortpathlist_toDF)
    shortpathlist_toDF.to_excel(os.path.join(os.getcwd(),catName+'DF.xlsx'))
    return shortpathlist_toDF
imDF = get_shortPaths('medical_instrument2',extension='.jpg')