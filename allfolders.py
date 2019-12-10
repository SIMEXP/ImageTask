# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:05:32 2019

@author: Francois
"""

import os
from PIL import Image
from os.path import basename as bname
from os.path import dirname as dname
from os.path import join

#def getfolders(fname,prefix):
#    for allim in os.walk(join(os.getcwd(),fname)):
#        for picture in allim[2]:
#            picpath = join(allim[0],picture)
#            allfolders = picpath.split(sep="\\")
#            for item in range(allfolders.index(fname),len(allfolders)):
#                newdirs = allfolders
#                newdirs[item] = prefix+newdirs[item]
#                apath = [[join(newdirs[item],newdirs[item+1])]for item in range(len(newdirs)+1)]
#                apath = apath[item]
#                try:
#                    os.system("mkdir {}".format(apath))
#                except apath == picpath:
#                    pass
#                except:
#                    os.system("mkdir {}".format(apath)) == 1
#                    pass
#            img = Image.open(picpath)
#            path = [[join(newdirs[item],newdirs[item+1])] for item in range(len(newdirs)-1)]
#            path = apath[item]
#            newimpath = join(path,prefix+picture)
#            img.save(newimpath, 'JPEG', quality=90)
#    return allfolders
def getfolders(fname,prefix):
    for allim in os.walk(join(os.getcwd(),fname)):
        for picture in allim[2]:

#prefix = '500_'
#fname = 'birdies_test2'
#getfolders(fname, prefix)
#folders = getfolders('birdies_test2')
#impath = 'C:\\Users\\Francois\\GitHub\\ImageTask\\bird\\chicken\\body_chicken\\body_chicken01_f_5922921580_57ebe68629_o.jpg'
#os.system("mkdir {}".format(impath))