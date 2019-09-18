# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:49:12 2019

@author: Francois
"""

import os # Import this one 1st if not already in the directory of the task
import pandas as pd
#import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from secrets import choice
from secrets import randbelow
from typing import Sequence
#from psychopy import logging
#@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@@@ @@@
#logging.console.setLevel(logging.INFO)
# Returns unidimensional list from nested list (any nesting level)
#def flatten(nestedlst):  
#	return [bottomElem for sublist in nestedlst 
#            for bottomElem in (flatten(sublist)
#            if (isinstance(sublist, Sequence)
#            and not isinstance(sublist, str)) else [sublist])
#           ]
def flatten(nestedlst):
    flatten_list = []
    for sublist in nestedlst:
        if not(isinstance(sublist, Sequence)):
            flatten_list.append(sublist)
        else:
            recur_flatten = flatten(sublist)
            flatten_list += recur_flatten
    return flatten_list
    
# Insert element to random index in list
def random_insert(lst, item): 
    return lst.insert(randbelow(len(lst)+1), item)

class Categories(object):
     #Allows to create a single Categories object
    @classmethod
    def filePathlist(cls, maindir):
        for maindir, dirnames,filenames in os.walk(os.path.abspath(maindir)):
            filePathlist = [os.path.join(maindir, filename)
            for filename in filenames if '.jpg' in filename]
            return (sorted(filePathlist))
    #Allows to create a single Categories object
    @classmethod     
    def categCreate(cls,maindir):
        imMatrix = [cls.filePathlist(os.path.join(maindir,dirname))
        for dirname in os.listdir(maindir)]
        return tuple(imMatrix)
   
#categs = loadCategsAsList()
class Trials(object):
    def __init__(self,numTrial,nStim,*args,**kwargs):
#        super().__init__(**kwargs)
        self.numTrial = numTrial
        self.nStim = nStim
        self.categs = [Categories.categCreate(maindir) 
                      for maindir in os.listdir(os.getcwd()) 
                      if maindir.startswith('500_')]
    #Creates a list containing all Categories objects (all at once)
#    def loadCategsAsList(self):
#        categs = 
#        return categs
    def randImage(self):
        randCateg = randbelow(len(self.categs)-1)
        randSubcat = randbelow(len(self.categs[randCateg]))
        randIm = choice(self.categs[randCateg][randSubcat])
        return randIm
   
    def getStims(self):
        self.Encodingstims = [[self.randImage() for stim in range(self.nStim)]
                             for trial in range(self.numTrial)]
        
        self.Distractors = [[self.randImage() for stim in range(self.nStim-2) 
                           if stim not in flatten(self.Encodingstims)]
                           for trial in range(self.numTrial)]
        return self.Distractors
trialos = Trials(2,4).getStims()

#        return self.Distractors
        
#        self.trialdict = {'Encoding':self.Encodingstims,'Distractors':self.Distractors}
#        return trialdict
