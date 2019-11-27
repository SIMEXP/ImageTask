# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:20:50 2019

@author: Francois
"""
from PIL import Image
import psychopy
from psychopy import visual
from psychopy import event


import os
from secrets import randbelow as rb

cwd = os.getcwd()
    
class ImageCategories(object):
   
    def __init__(self,nTrials,nStim):
       self.nTrials = nTrials
       self.nStim = nStim
       self.trialdict = self.loadimages()
       
    def loadimages(self):
        imlist = []
        shufims = list(range(self.nTrials))
        imdir = os.path.join(os.getcwd(),'images')
        for root, dirs, images in os.walk(imdir):
            for image in images:
                if '.jpeg' in image:
                    imlist.append(os.path.join(root,image))
        for ntrial in range(self.nTrials):
            shufims[ntrial] = [imlist[rb(len(imlist))] 
                                  for nstim in range(self.nStim)
                                  if imlist[rb(len(imlist))] 
                                  not in shufims]
        trialdict = {'trial'+str(ntrial):shufims[ntrial]
                    for ntrial in range(self.nTrials)}
        return trialdict
                   
trialdict1 = ImageCategories(4,80).loadimages()