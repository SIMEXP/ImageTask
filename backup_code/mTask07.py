# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:49:12 2019

@author: Francois
"""

import os # Import this one 1st if not already in the directory of the task
import pandas as pd
#import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
#from PIL import Image
from secrets import choice
from secrets import randbelow as rb
from flatten import flatten
from randInsert import randInsert
#from psychopy import logging
#@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@
#logging.console.setLevel(logging.INFO)

class Categories(object):
     #Allows to create a single Categories object
    def __init__(self,numTrial,nStim):
        self.numTrial = numTrial
        self.nStim = nStim
        self.graySquare = os.path.abspath('gray_square_318364508_17317b9b36_o.jpg')
        self.categs = [Categories.categCreate(maindir) 
                      for maindir in os.listdir(os.getcwd()) 
                      if maindir.startswith('500_')]
        
        self.Encod = [[self.randImage() for stim in range(self.nStim)]
                     for trial in range(self.numTrial)]
        
        self.EnStims = [randInsert(self.Encod[trial],
                                    self.graySquare)
                       for trial in range(self.numTrial)]
        
        
        self.Targs = [choice(self.Encod[trial]) 
                     for trial in range(self.numTrial)]
        
        self.Distractors = [[self.randImage() for stim in range(self.nStim) 
                           if stim not in flatten(self.Encod)]
                           for trial in range(self.numTrial)]
        
        self.recStims = [randInsert(self.Distractors[trial],
                                        self.Targs[trial])
                        for trial in range(self.numTrial)]

        self.imDF = pd.DataFrame.from_dict({'Encoding':self.EnStims,
                                            'Recall':self.recStims})
        
        self.trialslist = list(
                              pd.DataFrame.to_dict(
                                                  self.imDF,
                                                  orient='index').values())

    @classmethod
    def filePathlist(cls, maindir):
        for maindir, dirnames,filenames in os.walk(os.path.abspath(maindir)):
            filePathlist = [os.path.join(maindir, filename)
            for filename in filenames if '.jpg' in filename]
            return (sorted(filePathlist))
    #Allows to create a single Category object
    @classmethod     
    def categCreate(cls,maindir):
        imMatrix = [cls.filePathlist(os.path.join(maindir,dirname))
        for dirname in os.listdir(maindir)]
        return tuple(imMatrix)
    
    def randImage(self):
        randCateg = rb(len(self.categs)-1)
        randSubcat = rb(len(self.categs[randCateg])-1)
        randIm = choice(self.categs[randCateg][randSubcat])
        return randIm
#cats = Categories(2,6)
#gris = Image.open(cats.graySquare)

#encod = cats.EnStims
#recstms = cats.recStims
#trials = cats.trialslist