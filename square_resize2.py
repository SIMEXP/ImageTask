# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:16:38 2019

@author: Francois
"""
from PIL import Image
import os
import platform
import pandas as pd
from shutil import move as mv
from tqdm import tqdm
from flatten import flatten

def square_resize2(catName,size=(500,500),extension='.jpeg'):
#def square_resize2(catName):

    """
	Prepare images for the scanner

	This function:
        ames images to a shorter name
		Saves web name/image ID to csv (for references)
		Changes apect ratio to square (cropping)
		Uniformizes image files extensions
		Resizes images to desired size in pixels
		Saves resized images to new location (no overwriting)

	Parameters
	----------
	catName: type = str
		name of category images directory (ex: 'outdoor_sport')

	size: type = tuple
		Tuple (width, length) indicating desired size in pixels
			type(width) and type(length) = int
            width & length should be equal

	extension: type = str
		Desired file extension for images as string

	Returns
	-------
	None
    """
    
    cwd = os.getcwd()
    check = platform.system()
    sources = pd.read_csv(cwd + '\\' + 'sources.csv')
    references = sources['reference'].tolist()
#    altRefs = [ref.upper() for ref in refs] #Checking for mistaken CAPS
#    references = refs+altRefs
    shortpathlist_toDF = []
    shortpathlist = []
                         #Adapting the directory paths to appropriate OS
    if check == 'Windows':
        catPath = cwd +'\\'+ catName
    else:
    	catPath = cwd +'/'+ catName
                                           #Accessing files
    subDirs = [os.path.join(catPath,dirname) 
              for dirname in os.listdir(catPath)]
    fPaths = flatten([[os.path.abspath(os.path.join(subDir,filename))
             for filename in os.listdir(subDir)]
             for subDir in subDirs.__iter__()])                                   

                                    #Counting subdirectories & images
    for subDir in subDirs.__iter__():
        extTest = os.path.splitext(subDir)[1]
        if extTest == ' ' and len(subDir) != 16:
            print(subDir + ' has '+str(len(subDir))+' subcategories')
        elif extTest != ' ' and len(subDir) != 20:
            print(subDir+' has '+str(len(subDir))+' images')
            break

                                   #Rename images  & save references to csv
    for imPath in fPaths.__iter__():
        for ref in references.__iter__():
            refInd = imPath.find(ref)
            if refInd != -1:
                longpath, ext = os.path.splitext(imPath)
                shortpath = longpath[:longpath.find(ref)]+extension
                shortpathlist.append(shortpath)
                shortpathlist_toDF.append((shortpath,imPath))
                mv(imPath,shortpath)
    shortpathlist_toDF = pd.DataFrame(shortpathlist_toDF)
    shortpathlist_toDF.to_excel(os.path.join(os.getcwd(),catName+'DF.xlsx'))

                                      #Resize images & save to 'resizedPath'
    for newpath in tqdm(shortpathlist):
            subcatPath, imName = os.path.split(newpath)
            subcatName = os.path.basename(subcatPath)
            newCatPath = os.path.join(cwd, '500_' + catName)
            newSubcatPath = os.path.join(newCatPath, "500_"+subcatName)
            newName = "500_"+ os.path.basename(newpath)
            resizedPath = os.path.join(newSubcatPath,newName)
            if not '500_' in subcatPath:
                im = Image.open(newpath)
                im = im.convert("RGB")  #Converts 'im' to RGB to save in JPEG
                width, height = im.size
                if width > height:
                    im = im.crop(((width-height)/2,0,(width+height)/2,height))
                elif width < height:
                    im = im.crop((0,(height-width)/2,width,(height+width)/2))
                imResized = im.resize(size, Image.ANTIALIAS)
                os.system("mkdir {}".format(newCatPath))
                os.system("mkdir {}".format(newSubcatPath))
                imResized.save(resizedPath,'JPEG', quality = 90)
square_resize2('vehicle2',size=(500,500),extension='.jpeg')