#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:08:02 2019

@author: francois
"""

import os
from os.path import join
from PIL import Image
from tqdm import tqdm
import imdirect

def square_image():
    '''
    Crops all images in a directory to square aspect ratio.
    '''
    imdirect.monkey_patch()
    for allim in os.walk(os.getcwd()):
        for picture in tqdm(allim[2]):
            picpath = join(allim[0], picture)
            image = Image.open(picpath)
            if image.mode != 'RGB':
                image.convert("RGB")
            if image.size[0] > image.size[1]:
                image = image.crop(((image.size[0]-image.size[1])/2,
                                    0,
                                    (image.size[0]+image.size[1])/2,
                                    image.size[1]))
            elif image.size[0] < image.size[1]:
                image = image.crop((0,
                                    (image.size[1]-image.size[0])/2,
                                    image.size[0],
                                    (image.size[1]+image.size[0])/2))
            image.save(picpath, 'JPEG', quality=90)
square_image()
