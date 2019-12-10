# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:16:38 2019

@author: Francois
"""
import imdirect
import os
import pandas as pd
from PIL import Image
from shutil import move as mv
from tqdm import tqdm
from taskfunctions import flatten

def square_resize2(folderName,size=(500,500),extension='.jpeg'):
    """
	Prepare images for the scanner

	This function:
        Reames images to a shorter name
		Saves web name/image ID to csv (for references)
		Changes apect ratio to square (cropping)
		Uniformizes image files extensions
		Resizes images to desired size in pixels
		Saves resized images to new location (no overwriting)

	Parameters
	----------
	folderName: type = str
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
                          #Fixes unexpected image rotation while saving
    imdirect.monkey_patch()   
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
        folderPath = cwd +'\\'+ folderName
    else:
    	folderPath = cwd +'/'+ folderName

    subDirs = [os.path.join(folderPath,dirname) 
                  for dirname in os.listdir(folderPath)]
        
                                               #Accessing files

    fPaths = flatten([[os.path.abspath(os.path.join(subDir,filename))
             for filename in os.listdir(subDir)]
             for subDir in subDirs.__iter__()])                                   

                                   #Rename images  & save references to csv
    for impath in fPaths.__iter__():
        for ref in references.__iter__():
            refInd = impath.find(ref)
            if refInd != -1:
                longpath, ext = os.path.splitext(impath)
                shortpath = longpath[:longpath.find(ref)]+extension
                shortname = os.path.basename(shortpath)
                webname = impath[refInd+len(ref):]
                imageID, imageExt = os.path.splitext(webname)
                shortpathlist.append(shortpath)
                shortpathlist_toDF.append((shortname,
                                           ref,imageID,imageExt))
                mv(impath,shortpath)
    shortpathlist_toDF = pd.DataFrame(shortpathlist_toDF)
    shortpathlist_toDF.to_excel(os.path.join(os.getcwd(),folderName+'DF.xlsx'))

                                      #Resize images & save to 'resizedPath'
    for newpath in tqdm(shortpathlist):
            prefix = str(size[0])+'_'
            subfolderPath, imName = os.path.split(newpath)
            subfolderName = os.path.basename(subfolderPath)
            newfolderPath = os.path.join(cwd, prefix + folderName)
            newSubfolderPath = os.path.join(newfolderPath,
                                            prefix+subfolderName)
            newName = prefix + os.path.basename(newpath)
            resizedPath = os.path.join(newSubfolderPath,newName)
            if not prefix in subfolderPath:
                im = Image.open(newpath)
                im = im.convert("RGB")  #Converts 'im' to RGB to save in JPEG
                width, height = im.size
                if width > height:
                    im = im.crop(((width-height)/2,0,(width+height)/2,height))
                elif width < height:
                    im = im.crop((0,(height-width)/2,width,(height+width)/2))
                imResized = im.resize(size, Image.ANTIALIAS)
                os.system("mkdir {}".format(newfolderPath))
                os.system("mkdir {}".format(newSubfolderPath))
                imResized.save(resizedPath,'JPEG', quality = 90)
#properIndex('face_cardinal')
square_resize2('cardinal_test',size=(500,500),extension='.jpeg')