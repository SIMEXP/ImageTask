# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:06:06 2019

@author: Francois
"""
        #stimpos = [(250.0, 250.0),(-250.0, -250.0),(250.0, -250.0),(-250.0, -250.0)] #Possibly replacing randSign()

from pandas import DataFrame as df
from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from Categories import Categories
from randSign import randSign

class Encoding(object):
    def __init__(self):
        self.categs = Categories(2,5).trialslist
        self.trials = data.TrialHandler(self.categs,
                                        1, 
                                        method='sequential')
        
        
        self.win = visual.Window(size=(1000, 1000), 
                                color=(0, 0 , 0), 
                                units = 'pix')
        self.instructionStart = visual.TextStim(self.win, 
                                               text = 'Memorize the \
                                               following images and \
                                               their location on screen.\
                                               Press space to start.')
        self.poslist = []        

    def setstimpos(self):
        self.stimpos = (randSign()*250, randSign()*250)
        return self.stimpos

            
    def runTask(self): # Shows stimuli in each trial list in "trials"(also list) 
        self.instructionStart.draw()
        self.win.flip()
        event.waitKeys(keyList=["space"],clearEvents=False)
        for eachTrial in range(len(self.trials.trialList)-1):
            stims = self.trials.trialList[eachTrial]['Encoding']
            for stim in range(len(stims)-1):
                stimulus = visual.ImageStim(self.win,
                                            image = stims[stim], 
                                            color=(1,1,1), 
                                            pos = self.setstimpos(), 
                                            size = (500, 500))
                stimulus.draw()
                self.win.flip()
                self.poslist.append(stimulus.pos)
                core.wait(1)

        return self.poslist
        self.win.close()
task = Encoding().runTask()            
#
#trialos = Encoding()
#help(trialos.categs)
#trialosDF = df(trialos)