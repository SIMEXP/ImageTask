# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:20:50 2019

@author: Francois
"""
import os
from secrets import choice
from secrets import randbelow as rb

class ImageCategories(object):
   def __init__(self,nTrials,nStims):
       self.nTrials = nTrials
       self.nStims = nStims
       
   def loadImages(self):
       cwd = os.getcwd()
       categories = [categ for categ in os.listdir(cwd) if categ.startswith('500_')]
       for root, dirs, images in os.walk(cwd):
           images = [image for image in images
                    if image.endswith('.jpeg')]
       return categories
catTest = ImageCategories(2,20).loadImages()