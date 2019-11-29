# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:19:43 2019

@author: Francois
"""
import os
from taskfunctions import properIndex
foldername = 'bird'
def getdirnames(folderName):   
    cwd = os.getcwd()
    folderpath = os.path.join(cwd,foldername)
    impaths = []
    for root,dirs,files in os.walk(folderpath):
        dpaths = []
        for dname in dirs:
            dpaths.append([os.path.join(root,dname)])
        for file in files:
            fpath = os.path.join(root,file)
            if os.path.isfile(fpath) and file.endswith('.jpeg') == True:
                for dpath in range(len(dpaths)):
                    if os.path.split(fpath)[0] == dpaths[dpath]:
                        dpaths[dpath].append(fpath)
                impaths.append(fpath)
                
            
#        for dname in dirs:
#            properIndex(dname)
#        for file in files:
#            fpath = os.path.join(root,file)
#            for dname in dirs:
#                if os.path.dirname(fpath) == dname:
#                    
#            for dname in dirs:
#                if os.path.dirname(file) == dname:
#                    fpaths[dname].append(file)
                    
#                fpaths.append(os.path.join(root,file))
##        item = Image.open(os.path.realpath(item))
#        dirpaths = [os.path.join(root,dname)
#                   for dname in dirs]
##        groupedfiles = [[fpath for fpath in fpaths.__iter__()]
##                       for dirpath in dirpaths.__iter__()
##                       if os.path.split(fpath)[0] == dirpath]
#        groupedfiles = [[fpath for fpath in fpaths]
#                       for dname in dirs
#                       if os.path.split(fpath)[0] == dirpath]
#

    return impaths
#        for dirpath in dirpaths:
#            properIndex(dirpath)
        
groupedfiles = getdirnames('bird')
#    subDirs = [os.path.join(root,dname) 
#              for dname in dirs
#              if os.path.isdir(os.path.join(root,dname)) == True]

#subDirectories = [os.path.join(folderPath,dname) 
#                  for dname in os.listdir(folderPath)]