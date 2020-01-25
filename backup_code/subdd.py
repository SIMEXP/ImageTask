# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:49:58 2019

@author: Francois
"""

import os
from os.path import abspath
from os.path import basename as bname
from os.path import dirname as dname
from os.path import join
from tqdm import tqdm

def name_index(fpath):
    '''
    Renames all files in a directory accordingly to parent folder's name.
    Naming template: parent_folder_name01 to parent_folder_nameXX
    '''
    fpath = abspath(fpath)
    for allpics in os.walk(fpath):
        for picture in tqdm(allpics[2]):
            os.rename(join(allpics[0], picture), join(allpics[0],
                      bname(dname(join(allpics[0],picture)))))


