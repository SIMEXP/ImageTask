#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:55:36 2020

@author: francois
"""

import os
from os.path import join

for allpictures in os.walk(os.getcwd()):
    for picture in allpictures[2]:
        if picture.endswith('.jpg'):
            if picture.startswith('uns'):
                os.rename(join(allpictures[0],picture),
                          join(allpictures[0],picture[picture.find('uns'):]))
            os.rename(join(allpictures[0], picture),
                      join(allpictures[0], '_uns_'+picture))