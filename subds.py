# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:47:44 2019

@author: Francois
"""

import os
import shutil


fname = 'animate_test'
prefix = '500_'
def ignorefiles(fname):
    for allim in os.walk(fname):
        ig_f =  [f for f in allim[2] if os.path.isfile(os.path.join(fname, f))]
        return ig_f
ig_f = ignorefiles(fname)
shutil.copytree(os.path.abspath(fname), os.path.join(os.path.split(os.path.abspath(fname))[0], prefix+fname), ignore= (item for item in ig_f.__iter__()).yield


#    for picture in allim[2]:
#        picpath = os.path.join(allim[0],picture)
#        paths = picpath.split(sep='\\')
#        fpath = paths.join((paths[item],paths[item+1]) for item in range(0,paths.index(fname)))
#        print(fpath)
#    for subd in allim[1]:
#        root = str(allim[0])
#        root = root.replace(fname, prefix+fname, 1)
#        root = os.path.join(root,prefix+subd)
##        if 'body_part_' in subd:
##            root = root.replace(os.path.basename(os.path.dirname(subd)),
##                                prefix+os.path.basename(os.path.dirname(subd)),
##                                1)
#    #        subdpath = os.path.join(allim[0],subd)
#    #        subdpath = subdpath.replace('Birds', prefix+'Birds')
#        print(root)
##        for img in allim[2]:
##            impath = os.path.join(allim[0], subd, img)
#subds = os.listdir()
#for subd in subds:
#    subd = os.path.abspath(subd)
#    for subdd in os.listdir(subd):
#        if os.path.isdiros.path.join(subd, subdd):
#            sentence = ['this','is','a','sentence']
#>>> '-'.join(sentence)
#'this-is-a-sentence'