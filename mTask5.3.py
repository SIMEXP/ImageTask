# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:18:09 2019

@author: Francois
"""
import os # Import this one 1st if not already in the directory of the task
import pandas as pd
import secrets # secrets module prefered to default module "random" Generates cryptographically strong random numbers 
from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from typing import Sequence

def flatten(nestedlst):  # Returns a list containing all items listed in a list of sublists (for any nesting level) on the same level
	return [bottomElem for sublist in nestedlst for bottomElem in (flatten(sublist) if (isinstance(sublist, Sequence) and not isinstance(sublist, str)) else [sublist])]

def random_insert(lst, item): # Insert element to random index in a list 
    return lst.insert(secrets.randbelow(len(lst)+1), item)

class Categories(object):
    @classmethod #Allows to create a single Categories object
    def categCreate(cls,maindir):
        def filePathlist(maindir):
            for maindir, dirnames, filenames in os.walk(os.path.abspath(maindir)):
                filePathlist = [os.path.join(maindir, filename)for filename in filenames if '.jpg' in filename]
                return tuple(sorted(filePathlist))
        imMatrix = [filePathlist(os.path.join(maindir,dirname)) for dirname in os.listdir(maindir)]
        return tuple(imMatrix)
    @classmethod #Creates a list containing all Categories objects (all at once)
    def loadCategsAsList(cls):
        categories = [Categories.categCreate(maindir) for maindir in os.listdir(os.getcwd()) if '500_' in maindir]
        return categories
class Trials(Categories):
    def __init__(self,numTrial,nStim,*args,**kwargs):
        super().__init__(**kwargs)
        self.numTrial = numTrial
        self.nStim = nStim
        self.categories = Categories.loadCategsAsList()
        self.Encodingstims = [[secrets.choice(self.categories[secrets.randbelow(len(self.categories))][secrets.randbelow(16)])for stim in range(self.nStim)]for trial in range(self.numTrial)]
        self.Distractors = [[secrets.choice(self.categories[secrets.randbelow(len(self.categories))][secrets.randbelow(16)])for stim in range(self.nStim-2) if stim not in flatten(self.Encodingstims)]for trial in range(self.numTrial)]
        self.Targets = [secrets.choice(self.Encodingstims[trial]) for trial in range(self.numTrial)]
        self.imDF = pd.DataFrame.from_dict({'Encodingstims':self.Encodingstims,'Distractors':self.Distractors,'Targets':self.Targets})
        self.trialslist = list(pd.DataFrame.to_dict(self.imDF,orient='index').values())
trials = data.TrialHandler(Trials(2,8).trialslist, 1, method='sequential')

def runtask(trials):
    win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
    positions = list()
    eachTrial = 0
    while eachTrial <= len(trials.trialList)-1:
        def encodingphase(win): # Shows stimuli in each trial list in "trials"(also list) 
            def randSign():#randomly generates 1 or -1 (quadrant position)
                if secrets.randbelow(2) == 0:
                    return 1
                else:
                    return -1 
                #stimpos = [(250.0, 250.0),(-250.0, -250.0),(250.0, -250.0),(-250.0, -250.0)] #Possibly replacing randSign()
            instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press space to start.') 
            instructionStart.draw()
            win.flip()
            event.waitKeys(keyList=["space"],clearEvents=False)
            for stim in range(len(trials.trialList[eachTrial]['Encodingstims'])-1):
                stimulus = visual.ImageStim(win,image = trials.trialList[eachTrial]['Encodingstims'][stim], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
                stimulus.draw()
                win.flip()
                core.wait(1)
        def recall(positions,win):
            instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
            ansRecMessage = visual.TextStim(win, text='Answer recorded')
            random_insert(trials.trialList[eachTrial]['Distractors'],trials.trialList[eachTrial]['Targets'])
            for recallstim in range(len(trials.trialList[eachTrial]['Distractors'])-1):
                instruction1.draw()
                win.flip()
                core.wait(2.5)
                stimulus = visual.ImageStim(win,trials.trialList[eachTrial]['Distractors'][recallstim],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
                stimulus.draw()
                win.flip()
                keys = event.waitKeys(keyList=['y','n']) 
                if  "y" in keys:
                    instruction2 = visual.TextStim(win, text='Where have you seen it? Press 0, 1, 2 or 3 to answer')
                    instruction2.draw()
                    win.flip()
                    keys = event.waitKeys(keyList=["0","1","2","3"])                    
                ansRecMessage.draw()
                win.flip()
                core.wait(1.0)
        encodingphase(win)
        recall(positions,win)
        eachTrial +=1
    else:
        instructionEnd = visual.TextStim(win, text='Thank you for your time, goodbye!')
        instructionEnd.draw()
        win.flip()
        core.wait(2.5)
        return positions
        win.close
#        core.quit #Would this do the trick to exit the window without restarting the kernel?
positions = runtask(trials)
