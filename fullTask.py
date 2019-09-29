# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:15:24 2019

@author: Francois
"""

import os
import numpy as np
import pandas as pd
from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from Categories import Categories
from randSign import randSign

class imTask(object):
    def __init__(self,whichTrial,nTrial,nStim):
        self.whichTrial = whichTrial
        self.nTrial = nTrial
        self.nStim = nStim
        self.categs = Categories(nTrial,nStim)
        self.encDict = self.categs.encDF.to_dict(orient="index")
        self.thisEncTrial = self.encDict[self.whichTrial]
        self.recDict = self.categs.recDF.to_dict(orient="index")
        self.thisRecTrial = self.recDict[self.whichTrial]
        self.thisTrialTarg = self.categs.Targs[self.whichTrial]
#        self.encTask = Encoding(nTrial,nStim)
        self.poslist = []
        self.stimpos = {'0':np.array((-250.0, 250.0)),
                        '1':np.array((250.0, 250.0)),
                        '2':np.array((250.0, -250.0)),
                        '3':np.array((-250.0, -250.0))}
        
        self.encInstStartText = '''\
        ... Memorize the following images and
        ... their location on screen.\
        ... Press space to start.\
                                '''.format()
        
        self.recInstStartText = '''\
        ... A series of {x} images will appear.
        ... Indicate if shown image corresponds to a previously seen image
        ... and in which quadrant it has appeared earlier.
        ... Press SPACE to start\
                             '''.format(x=self.nStim+1)
        
        self.recInstText1 = '''\
        ... Have you seen this picture before?
        ... If yes, press "y". If not, press "n".\
                         '''.format()
        
        self.recInstText2 = '''\
        ... Where have you seen it? 
        ... Press 0, 1, 2 or 3 to answer\
                         '''.format()
                         
        self.recInstPosText = '''\
        ... Where have you seen it?
        ... 0 = upper-left, 1 = upper-right
        ... 2 = lower-left, 3 = lower-right\
                           '''.format()
        
        self.ansSaveText = 'Answer saved!'
        
        self.endText = 'Thank you for your time, goodbye!'

    def setstimpos(self):
        setpos = (randSign()*250, randSign()*250)
        return setpos     
#        self.trials = data.TrialHandler(self.stims,
#                                        1, 
#                                        method='sequential')
    def runEnc(self):
        self.win = visual.Window(size=(1000, 1000), 
                                color=(0, 0 , 0), 
                                units = 'pix')
        self.encInstStart = visual.TextStim(self.win, 
                                               text = self.encInstStartText)
        self.encInstStart.draw()
        self.win.flip()
        event.waitKeys(keyList=["space"])
        for stim in range(len(self.thisEncTrial)-1):
            stimulus = visual.ImageStim(self.win,
                                        self.thisEncTrial[stim],
                                        color=(1,1,1), 
                                        pos = self.setstimpos(), 
                                        size = (500, 500),
                                        name=self.thisEncTrial[stim])
            stimulus.draw()
            self.win.flip()
            stimTuple = (stimulus.name, stimulus.pos)
            self.poslist.append(stimTuple)
            core.wait(1)
        self.win.close()
        self.stimDF = pd.DataFrame(self.poslist)
#        self.stimDF.to_csv(os.getcwd()+'\\stimDF2.csv')
        return self.stimDF
    
    def getScore():
        answerlist = []
        encposlist = []
        thisTrialTarg = task.thisTrialTarg
        stimpos = {'0':np.array((-250.0, 250.0)),
                   '1':np.array((250.0, 250.0)),
                   '2':np.array((250.0, -250.0)),
                   '3':np.array((-250.0, -250.0))}
        
#        for key,value in stimpos.items():
#            value = rectask['PosAnsers']
#            key = stimpos.value
#            encposlist.append(key)
#        rectask.append(encposlist)
#        return rectask
#        
#        if rectask[]
#
#        for index in rectask.index:
#            if rectask['Stims']==thisTrialTarg:
#                if "y" in rectask['Recognition']:
#                    answerlist.append('recogOK')
#                elif "n" in rectask['Recognition']:
#                    answerlist.append('recogWrong')
#            
#            for answer in rectask['PosAnswer'][index]:
#                if answer != 'none':
#                    answer = stimpos[answer]
#                    answerlist.append(answer)
            
    def runRec(self):
        self.win = visual.Window(size=(1000, 1000), 
                                color=(0, 0 , 0), 
                                units = 'pix')
        
        self.recInstStart = visual.TextStim(self.win,
                                            text=self.recInstStartText)
        
        self.recInstPos = visual.TextStim(self.win,
                                          text=self.recInstPosText,
                                          pos=(0.0,-300))
            
        self.recInst1 = visual.TextStim(self.win,
                                        text=self.recInstText1,
                                        pos=(0.0,300))
        
        self.recInst2 = visual.TextStim(self.win,
                                        text=self.recInstText2)

        self.ansRec = visual.TextStim(self.win,
                                      text=self.ansSaveText)
        
        self.end = visual.TextStim(self.win, text=self.endText)
        
        self.stimNamelist = []
        self.recKeylist = []
        self.posKeylist = []
        self.recInstStart.draw()
        self.win.flip()
        
        event.waitKeys(keyList=["space"])
        for stim in range(len(self.thisRecTrial)-1):
            stimulus = visual.ImageStim(self.win,
                                        self.thisRecTrial[stim],
                                        color=(1,1,1), 
                                        pos = (0.0,0.0), 
                                        size = (500, 500),
                                        name=self.thisRecTrial[stim])
            self.recInst1.draw()
            self.recInst1.autoDraw = True
            stimulus.draw()
            self.win.flip()
            recKeys = event.waitKeys(keyList=['y','n'])
            if "y" in recKeys:
                self.recInst2.draw()
                self.win.flip()
                posKeys = event.waitKeys(keyList=["0","1","2","3"])
                self.posKeylist.append(posKeys)
                core.wait(1)
            elif "n" in recKeys:
                self.posKeylist.append("None")
            self.recKeylist.append(recKeys)
            self.stimNamelist.append(stimulus.name)
            self.ansRec.draw()
            self.win.flip()
            core.wait(1)
        self.TrialDict = {'Stims':self.stimNamelist,
                          'Recognition':self.recKeylist,
                          'PosAnsers':self.posKeylist}
        self.end.draw()
        self.win.flip()
        core.wait(2)
        self.win.close()
        return pd.DataFrame(self.TrialDict)

task = imTask(0,2,3)
encTask = task.runEnc()
rectask = task.runRec()   
#enc = Encoding(2,3).trials.trialList[0]['Encoding']