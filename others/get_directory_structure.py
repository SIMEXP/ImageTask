#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:22:05 2020

@author: francois
"""

from functools import reduce
import json
import os
from os import listdir as ls
from os.path import join
from os.path import basename as bname
from os.path import dirname as dname
import pandas as pd

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir

def imcount():
    imdict = {}
    for allimages in os.walk(os.path.relpath('neuromod_image_bank')):
        for folder in enumerate(allimages[1]):
            folderdict = {bname(dname(join(allimages[0],
                                           folder))):(folder,
                                                      len(ls(join(allimages[0],
                                                                  folder[1]))))}
            imdict[folder[0]] = folderdict      
            print(folderdict)
            print(folder, len(os.listdir(os.path.join(allimages[0],folder))))
image_dict = get_directory_structure('neuromod_image_bank')
image_df = pd.DataFrame(image_dict)
with open('image_dict.json', 'w') as fp:
    json.dump(image_dict, fp)