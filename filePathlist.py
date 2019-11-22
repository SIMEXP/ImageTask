# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:47:47 2019

@author: Francois
"""

import os
from secrets import choice

def filePathlist(maindir):
    """
    Lists full image paths in maindir as strings
    ...
    
    Parameters
    ----------
    maindir: type = str
        Name of image directory. 
        Must be in current working directory
    ...
    
    Return
    ------
    filePathlist: type = list
        List of all image fullpaths in a subcategory 
        (last one by default) in maindir. Meant to be called
        by 'categCreate()'.
    """
    for mainpath, dirnames,filenames in os.walk(os.path.abspath(maindir)):
        filePathlist = [os.path.join(mainpath,filename)
                       for filename in filenames 
                       if filename.startswith('500_')]               
        return (sorted(filePathlist))
#    for maindir, dirnames,filenames in os.walk(os.path.abspath(maindir)):
#        filePathlist = [os.path.join(maindir,dirname)
#                       for dirname in dirnames 
#                       if dirname.startswith('500_')]               
#        return (sorted(filePathlist))
fpl = filePathlist(cwd)

def getstimpaths(imDir,nStim=80):
    imDir_path = os.path.abspath(imDir)
    if imDir_path != os.getcwd():
        os.chdir(imDir_path)
    cwd = os.getcwd()
    images = []
    trialsList = []
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.startswith('500_') and file.endswith('.jpeg'):
                images.append(os.path.join(root,file))
    #    {trial: stims for (trial, stims) in iterable}
    for nTrial in range(int(len(images)/nStim)):
#        print(nTrial)
        key = 'Trial'+str(int(nTrial))
        value = [choice(images) for stim in range(nStim)]
        trial = (key,value)
        trialsList.append(trial)
    return trialsList

trialdict = getstimpaths(os.getcwd(),80)
    
#            trialDict = {key,value for (k,v) in range}
#                 print(file)
            
   