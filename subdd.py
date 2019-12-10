# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:49:58 2019

@author: Francois
"""

import os
from os.path import basename as bname
from os.path import dirname as dname
from os.path import join
from os.path import split
from tqdm import tqdm

def name_index(fname):
    fpath = join(os.getcwd(), 'inanimate')
    for allpics in os.walk(fpath):
        for picture in tqdm(allpics[2]):
            os.rename(join(allpics[0], picture), join(allpics[0],
                      bname(dname(join(allpics[0],picture)))))


