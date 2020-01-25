# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:23:41 2019

@author: Francois
"""

import os
from os.path import join
from os.path import splitext
import pandas as pd

def proper_index(folderName):
    '''Names and indexes images according to category'''
    cwd = os.getcwd()
    sources = pd.read_csv(join(cwd, 'sources.csv'))
    references = sources['reference'].tolist()

    folderpath = join(cwd,folderName)

    for root, dirs, files in os.walk(folderpath):
        counter = 1
        for file in files:
            impath = join(root,file)
            dirPath = os.path.dirname(impath)
            dName = os.path.basename(dirPath)
            if 'bodypart' in dName:
                dName = dName.replace('bodypart','body_part')
                newdir = dirPath.replace(os.path.basename(dirPath), dName)
                os.rename(dirPath, newdir)
            for ref in references.__iter__():
                refInd = file.find(ref)
                if refInd != -1:
                    suffix = file[refInd:]
                else:
                    suffix = ''
            if counter <= 9:
                okName = dName+'0'+str(counter)+suffix+splitext(impath)[0]
            elif counter >= 10:
                okName = dName + str(counter)+suffix+splitext(impath)[0]
            okPath,ext = splitext(join(root,okName))
            os.rename(impath,okPath+'.jpeg')
            counter +=1
            print(len(os.listdir(dirPath)))
