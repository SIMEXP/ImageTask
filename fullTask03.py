# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 04:40:42 2019

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
        '''
        Parameters
        ----------
        
        nTrial: number of runs for a subject
        
        nStim: number of new images used in each phase in a trial
        
        '''
        
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
        self.outputlist = []
        
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
        '''
        Randomly sets the position of stimuli durung encoding
        phase
        
        '''
        setpos = (randSign()*250, randSign()*250)
        return setpos
    
    def getTargPos(self,whichTrial):
        '''
        Returns a the position of target stimuli 
        (during encoding phase) as a tuple.
        '''
        for encstim in range(len(self.encStimlist)):
            stimTuple = self.encStimlist[encstim]
            if stimTuple[0] == self.thisTrialTarg:
                pos = stimTuple[1]
                return pos

    def getAnswers(self,whichTrial):
        '''
        Returns the answers based on keys pressed by subject
        in a list and adds this list as 'Answers' in 'self.TrialDict'.
        
        '''
        self.answerlist = []
        self.targetPos = self.getTargPos(whichTrial)
        tPos = self.getTargPos(whichTrial)
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
        self.TrialDict.update({'Answers':self.answerlist})
 

    def runTask(self, whichTrial):
        '''
        Launches the memory task. Saves each trial's dictionary
        to 'self.outputlist'.
        
        '''
        self.win = visual.Window(size=(1000, 1000), 
                                color=(0, 0 , 0), 
                                units = 'pix')   
        self.encTask = self.runEnc(whichTrial)
        self.recTask = self.runRec(whichTrial)
        self.getAnswers(whichTrial)
        self.outputlist.append(self.TrialDict)
        self.win.close()
        return self.outputlist

    def runEnc(self,whichTrial):
        '''
        Launches encoding phase.
        A series of 'self.nStim'+1 stimuli 
        ('self.nStim' images + 1 control stimulus (gray square))
        is shown to subject.
        Each images appears in a quadrant on screen. Subject must
        memorize ach image and its position (excepting control stimuli).
        
        '''
        self.encStimlist = []
        self.whichTrial = whichTrial
        self.thisEncTrial = self.encDict[self.whichTrial]

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
            
        self.stimDF = pd.DataFrame(self.encStimlist,
                                   columns=['encStims', 'encPos'])
        self.stimDict = self.stimDF.to_dict(orient="dict")
#        self.stimDF.to_csv(os.getcwd()+'\\stimDF2.csv')
        return self.encStimlist
                   
    def runRec(self,whichTrial):
        '''
        Launches Recall phase
        
        A series of 'self.nStim' +1 images ('self.nStim' new 
        images + 1 target image seen during encoding phase)
        is presented to subject.
        Subject must answer if image shown was seen or not
        during encoding phase. If so, user must indicate at
        which position it previously appeared (0,1,2,3).
        
        Answers and stimuli used are returned in a dictionary.
        Each run has a dictionary, listed in 'self.outputlist'.
        '''
        self.thisRecTrial = self.recDict[self.whichTrial]
        self.thisTrialTarg = self.categs.Targs[self.whichTrial]
        
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
        return self.TrialDict

task01 = imTask(2,3)
task01.runTask(0)
task01.runTask(1)
ans = task01.outputlist