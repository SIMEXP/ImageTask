# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 02:06:06 2019

@author: Francois
"""

from pandas import DataFrame as df
from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from Categories import Categories
from randSign import randSign

class Encoding(object):
    def __init__(self):
        self.categs = Categories(2,5)
        self.trials = data.TrialHandler(self.categs,
                                        1, 
                                        method='sequential')
trialos = Encoding()
help(trialos.categs)
trialosDF = df(trialos)
#print(dir(trialos))

#print(trialos.trialList[0])
#    def runtask(self):
#        win = visual.Window(size=(1000, 1000), 
#                            color=(0, 0 , 0), 
#                            units = 'pix')
#        eachTrial = 0
#        while eachTrial <= len(self.trials.trialList)-1:
#            stims = self.trials.trialList[eachTrial]['Encoding']
#            stimpos = (randSign()*250, randSign()*250)
#            def encodingphase(win): # Shows stimuli in each trial list in "trials"(also list) 
#    
#                    #stimpos = [(250.0, 250.0),(-250.0, -250.0),(250.0, -250.0),(-250.0, -250.0)] #Possibly replacing randSign()
#                instructionStart = visual.TextStim(win, 
#                                                   text = 'Memorize the \
#                                                   following images and \
#                                                   their location on screen.\
#                                                   Press space to start.') 
#                instructionStart.draw()
#                win.flip()
#                event.waitKeys(keyList=["space"],clearEvents=False)
#                for stim in range(len(stims)-1):
#                    stimulus = visual.ImageStim(win,
#                                                image = stims[stim], 
#                                                color=(1,1,1), 
#                                                pos = stimpos, 
#                                                size = (500, 500))
#                    stimulus.draw()
#                    win.flip()
#                    core.wait(1)