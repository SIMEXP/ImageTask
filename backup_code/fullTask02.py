# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:03:19 2019

@author: Francois
"""

import pandas as pd
from psychopy import core
#from psychopy import data
from psychopy import event
from psychopy import logging
from psychopy import visual
from Categories import Categories
from flatten import flatten
from randSign import randSign

class imTask(object):
    '''Runs the NeuroMod/CIMA-Q memory task
    '''
    def __init__(self,nTrial,nStim):
        self.log = logging.LogFile(f='imTaskLogFile')
        self.nTrial = nTrial
        self.nStim = nStim
        self.categs = Categories(nTrial,nStim)
        self.encDict = self.categs.encDF.to_dict(orient="index")
        self.recDict = self.categs.recDF.to_dict(orient="index")

        self.stimpos = {'0':(-250.0, 250.0),
                        '1':(250.0, 250.0),
                        '2':(250.0, -250.0),
                        '3':(-250.0, -250.0)}
        
        
        self.encInstStartText = '''\
            Memorize the following images and
            their location on screen.
            Press space to start.\
                                '''.format()
        
        self.recInstStartText = '''\
            A series of {x} images will appear.
            Indicate if shown image corresponds to a previously seen image
            and in which quadrant it has appeared earlier.
            Press SPACE to start\
                             '''.format(x=self.nStim+1)
        
        self.recInstText1 = '''\
            Have you seen this picture before?
            If yes, press "y". If not, press "n".\
                         '''.format()
        
        self.recInstText2 = '''\
            Where have you seen it? 
            Press 0, 1, 2 or 3 to answer\
                         '''.format()
                         
        self.recInstPosText = '''\
            Where have you seen it?
            0 = upper-left, 1 = upper-right
            2 = lower-left, 3 = lower-right\
                           '''.format()
        
        self.ansSaveText = 'Answer saved!'
        
        self.endText = 'Thank you for your time, goodbye!'

    def setstimpos(self):
        setpos = (randSign()*250, randSign()*250)
        return setpos
    
    def getTargPos(self):
        for encstim in range(len(self.encStimlist)):
            stimTuple = self.encStimlist[encstim]
            if stimTuple[0] == self.thisTrialTarg:
                pos = stimTuple[1]
                return pos

#for encstim in range(len(encstimlist01)):
#    stim = encstimlist01[encstim]
#    if stim[0] == targ01:
#        pos = stim[1]
#        print(pos)

    def getAnswers(self):
        tPos = self.getTargPos()
        for stim in range(len(self.TrialDict['recStims'])):
            shownStim = self.TrialDict['recStims'][stim]
            if shownStim == self.thisTrialTarg:
#                print('TargetFound!')
                if 'y' in self.TrialDict['Recognition'][stim]:
                    if self.TrialDict['StimPosAnswers'][stim] == tPos:
                        self.answerlist.append('recogOKposOK')
                    elif self.TrialDict['StimPosAnswers'][stim] != tPos:
                        self.answerlist.append('recogOKposWrong')
                elif 'n' in self.TrialDict['Recognition'][stim]:
                    self.answerlist.append('Miss')
            elif shownStim != self.thisTrialTarg:
                if 'y' in self.TrialDict['Recognition'][stim]:
                   self.answerlist.append('FalseAlarm')
                elif 'n' in self.TrialDict['Recognition'][stim]:
                    self.answerlist.append('RejectOK')
        return self.answerlist
            
    def runEnc(self, whichTrial):
        self.whichTrial = whichTrial
        self.thisEncTrial = self.encDict[self.whichTrial]
        self.encStimlist = []
        self.win = visual.Window(size=(1000, 1000), 
                                color=(0, 0 , 0), 
                                units = 'pix')
        self.encInstStart = visual.TextStim(self.win, 
                                            text = self.encInstStartText)
        self.encInstStart.draw()
        self.win.flip()
        event.waitKeys(keyList=["space"])
        for stim in range(len(self.thisEncTrial)):
            encstim = visual.ImageStim(self.win,
                                        self.thisEncTrial[stim],
                                        color=(1,1,1), 
                                        pos = self.setstimpos(), 
                                        size = (500, 500),
                                        name=self.thisEncTrial[stim])
            encstim.draw()
            self.win.flip()
            encStimTuple = (encstim.name, tuple(encstim.pos))
                
            self.encStimlist.append(encStimTuple)
            core.wait(1)
            
        self.win.close()
        self.stimDF = pd.DataFrame(self.encStimlist,
                                   columns=['encStims', 'encPos'])
        self.stimDict = self.stimDF.to_dict(orient="dict")
#        self.stimDF.to_csv(os.getcwd()+'\\stimDF2.csv')
        return self.encStimlist
                   
    def runRec(self):
        self.thisRecTrial = self.recDict[self.whichTrial]
        self.thisTrialTarg = self.categs.Targs[self.whichTrial]
        self.targetPos = self.getTargPos()
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
        posAnsKeys= []
        self.stimPosAnswers = []
        self.recInstStart.draw()
        self.win.flip()
        
        event.waitKeys(keyList=["space"])
        for stim in range(len(self.thisRecTrial)):
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
            if 'y' in recKeys:
                self.recInst2.draw()
                self.win.flip()
                posKeys = event.waitKeys(keyList=['0','1','2','3'])
                posAnsKeys.append(posKeys)
                core.wait(1)
            elif 'n' in recKeys:
                posAnsKeys.append('None')
            self.posKeylist = flatten(posAnsKeys)
            self.recKeylist.append(recKeys)
            self.stimNamelist.append(stimulus.name)
            self.ansRec.draw()
            self.win.flip()
            core.wait(1)
        for posKey in range(len(self.posKeylist)):
            answer = self.posKeylist[posKey]
            if answer != 'None':
                self.stimPosAnswers.append(self.stimpos[answer])
            elif answer == 'None':
                self.stimPosAnswers.append('None')
                                    
        self.TrialDict = {'recStims':self.stimNamelist,
                          'Recognition':flatten(self.recKeylist),
                          'PosKeylist':self.posKeylist,
                          'StimPosAnswers':self.stimPosAnswers}
        
        self.TrialDF = pd.DataFrame(self.TrialDict)
        self.end.draw()
        self.win.flip()
        core.wait(2)
        self.win.close()
        return self.TrialDict

task01 = imTask(2,3)
t01tpos = task01.getTargPos()
encdict01 = task01.encDict[0]
targ01 = task01.categs.Targs[0]
recdict01 = task01.recDict[0]
enctask01 = task01.runEnc(0)
rectask01 = task01.runRec(0) 
answerlist = task01.getAnswers()