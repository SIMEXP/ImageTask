# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 11:23:41 2019

@author: Francois
"""

import os
from unicodedata import lookup
import pandas as pd

def properIndex(folderName):
#    os.chdir('GitHub\\ImageTask')
    cwd = os.getcwd()
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    references = sources['reference'].tolist()
#    single = lookup("REVERSE SOLIDUS")
#    double = str(single+single)
    folderpath = os.path.join(cwd,folderName)
#    folderpath.replace(str(single),(double))

    for root, dirs, files in os.walk(folderpath):
        counter = 1
        for file in files:
            impath = os.path.join(root,file)
            dirPath = os.path.dirname(impath)
            dirName = os.path.basename(dirPath)
            if 'bodypart' in dirName:
                newDirName = dirName.replace('bodypart','body_part')
                dirName = newDirName
                print(dirName)
            for ref in references.__iter__():
                refInd = file.find(ref)
                if refInd != -1:
                    suffix = file[refInd:]
            if counter <= 9:
                okName = dirName  + '0' + str(counter) + suffix
            elif counter >= 10:
                okName = dirName + str(counter) + suffix
            okPath,ext = os.path.splitext(os.path.join(root,okName))
            os.rename(impath,okPath+'.jpeg')
            counter +=1
            print(len(os.listdir(dirPath)))
properIndex('body_sea_lion')