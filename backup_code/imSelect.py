# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:23:50 2019

@author: Francois
"""
###Lists all image files in current working directory, then selects a ramdom sample of nStim images from the list to another lsit.
from __future__ import division
import os
import random




def imSelect(nStim):
    def imPaths():
        imPathlist = []
        cwd = os.getcwd()
        for r, d, f in os.walk(cwd):
            for fileName in f:
                if '.jpg' in fileName:
                    imPathlist.append(os.path.join(r, fileName))
        return imPathlist
    imSelection = random.sample(imPaths(), nStim)
    return imSelection

trial1 = imSelect(15)