# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 01:49:01 2019

@author: Francois
"""

from psychopy import core
from psychopy import data
from psychopy import event
from psychopy import visual
from Categories import Categories
from randSign import randSign

class ImageTask(object):
    def __init__(self):
        self.trials = data.TrialHandler(Categories(2,5).trialslist, 1, method='sequential')
    def runtask(self):
        win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')
        eachTrial = 0
        while eachTrial <= len(self.trials.trialList)-1:
            def encodingphase(win): # Shows stimuli in each trial list in "trials"(also list) 
    
                    #stimpos = [(250.0, 250.0),(-250.0, -250.0),(250.0, -250.0),(-250.0, -250.0)] #Possibly replacing randSign()
                instructionStart = visual.TextStim(win, text = 'Memorize the following images and their location on screen. Press space to start.') 
                instructionStart.draw()
                win.flip()
                event.waitKeys(keyList=["space"],clearEvents=False)
                for stim in range(len(self.trials.trialList[eachTrial]['Encoding'])-1):
                    stimulus = visual.ImageStim(win,image = self.trials.trialList[eachTrial]['Encoding'][stim], color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
                    stimulus.draw()
                    win.flip()
                    core.wait(1)
            def recall(win):
                instruction1 = visual.TextStim(win, text='Have you seen this picture before? If yes, press "y". If not, press "n".')
                ansRecMessage = visual.TextStim(win, text='Answer recorded')
                for recStim in range(len(self.trials.trialList[eachTrial]['Recall'])-1):
                    instruction1.draw()
                    win.flip()
                    core.wait(2.5)
                    stimulus = visual.ImageStim(win,self.trials.trialList[eachTrial]['Recall'][recStim],color=(1,1,1), pos = (0.0, 0.0), size = (500, 500))
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
            recall(win)
            eachTrial +=1
        else:
            instructionEnd = visual.TextStim(win, text='Thank you for your time, goodbye!')
            instructionEnd.draw()
            win.flip()
            core.wait(2.5)
            win.close()
    #        core.quit #Would this do the trick to exit the window without restarting the kernel?
ImageTask().runtask()