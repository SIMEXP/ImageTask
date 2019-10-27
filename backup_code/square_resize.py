# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:58:45 2019

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

def get_shortPaths(catName,size=(500,500),extension='.jpg'):
    cwd = os.getcwd()
    check = platform.system()
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    references = sources['reference'].tolist()
    shortpathlist_toDF = []
    shortpathlist = []
        # Adapting the directory paths to the appropriate OS
    if check == 'Windows':
        catPath = cwd +'\\'+ catName
    else:
    	catPath = cwd +'/'+ catName
    subDirs = [os.path.join(catPath,dirname) 
              for dirname in os.listdir(catPath)]
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
                shortpath = longpath[:longpath.find(ref)]+ext
                shortpathlist.append(shortpath)
                shortpathlist_toDF.append((shortpath,imPath))
#                mv(imPath,shortpath)
    shortpathlist_toDF = pd.DataFrame(shortpathlist_toDF)
#    shortpathlist_toDF.to_csv(os.getcwd()+'\\'+'newNamesDF')

    for newpath in shortpathlist:
        subcatPath, imName = os.path.split(newpath)
        subcatName = os.path.basename(newpath)
       
        if not '500_' in subcatPath:
            im = Image.open(newpath)
            width, height = im.size
            if width > height:
                im = im.crop(((width-height)/2,0,(width+height)/2,height))
            elif width < height:
                im = im.crop((0,(height-width)/2,width,(height+width)/2))
            imResized = im.resize(size, Image.ANTIALIAS)
            
            newCatPath = os.path.join(cwd, '500_' + catName)
            os.system("mkdir {}".format(newCatPath))

            newSubcatPath = os.path.join(newCatPath, "500_"+subcatName)
            os.system("mkdir {}".format(newSubcatPath))
            imResized.save(os.path.join(newSubcatPath, "500_"+ os.splitext(imName)[0]), format=extension, quality = 90)

    shortpaths = pd.DataFrame((shortpathlist,fPaths))
##cat_name = input("Enter the category name (ie, the name of your folder): ")
square_resize('bathroom',size=(500,500),extension='.jpg')             
