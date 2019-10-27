# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 04:33:38 2019

@author: Francois
"""

import numpy as np
import pandas as pd
from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from Categories import Categories
from EncodingSubtask import Encoding
from randSign import randSign

class Recall(object):
    def __init__(self,nTrial,nStim):
        self.nTrial = nTrial
        self.nStim = nStim
        self.categs = Categories(nTrial,nStim)
        self.encResults = pd.read_csv(os.getcwd()+'\\stimDF.csv')
        self.stims = self.categs.recDF
        self.TargStims = self.categs.Targs
        
        self.stimpos = {'0':np.array((-250.0, 250.0)),
                        '1':np.array((250.0, 250.0)),
                        '2':np.array((250.0, -250.0)),
                        '3':np.array((-250.0, -250.0))}
        
        self.instStartText = '''\
        ... A series of {x} images will appear.
        ... Indicate if shown image corresponds to a previously seen image
        ... and in which quadrant it has appeared earlier.
        ... Press SPACE to start\
                             '''.format(x=len(self.stims)+1)
        
        self.inst1Text = '''\
        ... Have you seen this picture before?
        ... If yes, press "y". If not, press "n".\
                         '''.format()
        
        self.inst2Text = '''\
        ... Where have you seen it? 
        ... Press 0, 1, 2 or 3 to answer\
                         '''.format()
                         
        self.instPosText = '''\
        ... Where have you seen it?
        ... 0 = upper-left, 1 = upper-right
        ... 2 = lower-left, 3 = lower-right\
                           '''.format()
        
        self.ansSaveText = 'Answer saved!'
        
    def getScore(self):
        self.score = []
        for index in self.stims.index:
            for key in posKeys[index][stim]:
                answer = (self.stimulus.name,
                          key,
                          self.stimpos[self.posKeys[index][stim]])
                score.append(answer)
                return self.score
        
    def runRec(self):
        self.win = visual.Window(size=(1000, 1000), 
                                color=(0, 0 , 0), 
                                units = 'pix')
        
        self.instStart = visual.TextStim(self.win,
                                         text=instStartText)
        
        self.instPos = visual.TextStim(self.win,
                                       text=self.instPosText,
                                       pos=(0.0,-300))
        
        self.inst1 = visual.TextStim(self.win,
                                    text=self.inst1Text,
                                    pos=(0.0,300))
        
        self.instruction2 = visual.TextStim(self.win,
                                            text=self.inst2Text)

        self.ansRec = visual.TextStim(self.win,
                                      text=ansSaveText)
        
        for index in self.stims.index:
            self.instStart.draw()
            self.win.flip()
            event.waitKeys(keyList=["space"],clearEvents=False)
            for stim in range(self.nStim):
                self.inst1.draw()
                self.inst1.autoDraw = True
                nowStim = self.stims.loc[index][stim]
                self.stimulus = visual.ImageStim(self.win,
                                            image=nowStim,
                                            color=(1,1,1), 
                                            pos=(0.0,0.0),
                                            name=nowStim)
                self.stimulus.draw()
                self.win.flip()
                recKeys = event.waitKeys(keyList=['y','n'])
                
                if  "y" in recKeys:
                    self.instruction2.draw()
                    self.win.flip()
                    posKeys = event.waitKeys(keyList=["0","1","2","3"])
                    self.getScore()
                
                ansRecMessage.draw()
                win.flip()
                core.wait(1.0)
                self.win.flip()
                stimTuple = (self.stimulus.name, self.stimulus.pos)
                self.poslist.append(stimTuple)
                core.wait(1)
    self.win.close()
    self.stimDF = pd.DataFrame(self.poslist).to_csv(os.getcwd()+'\\stimDF.csv')
    return self.stimDF
        for recStim in range(len(self.trials.trialList[eachTrial]['Recall'])-1):
            
            stimulus = visual.ImageStim(win,self.trials.trialList[eachTrial]['Recall'][recStim],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
            stimulus.draw()
            win.flip()
            
    encodingphase(win)
    recall(win)
    eachTrial +=1
else:
    instructionEnd = visual.TextStim(win, text='Thank you for your time, goodbye!')
    instructionEnd.draw()
    win.flip()
    core.wait(2.5)
    win.close()