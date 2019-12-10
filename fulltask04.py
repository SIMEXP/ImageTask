# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:36:21 2019

@author: Francois
"""
from random import sample as randsmp
import pandas as pd
from psychopy import core
#from psychopy import data
from psychopy import event
#from psychopy import logging
from psychopy import visual
from taskfunctions import flatten
from taskfunctions import imMatrix
from taskfunctions import loadimages
from taskfunctions import sampling
from taskfunctions import setstimpos

class ImageTask():
    '''Runs the NeuroMod/CIMA-Q memory task
    '''
    def __init__(self, nstim, ntrial):
        '''
        Parameters
        ----------
        nTrial: number of runs for a subject
        nstim: number of new images used in each phase in a trial
        '''
        self.nstim = nstim
        self.ntrial = ntrial
        def loadstims(self):
            images = loadimages()
            invld = sampling(images, int(self.nstim/2), self.ntrial)
            encstims = imMatrix(sampling(images, self.nstim, self.ntrial,
                                         exclusives=invld))
            recstims = imMatrix([randsmp(self.encstims[ntrial]+invld[ntrial],
                                         len(self.encstims[0])+len(invld[0]))
                                 for ntrial in range(len(self.encstims))])
            stimdict = dict(zip([ntrial for ntrial in range(self.ntrial)],
                                [[encstims[ntrial],recstims[ntrial]]
                                 for ntrial in range(self.ntrial)]))
            return stimdict
#        self.messages = []
#        self.stimpos = {'0':(-250.0, 250.0),
#                        '1':(250.0, 250.0),
#                        '2':(250.0, -250.0),
#                        '3':(-250.0, -250.0)}
#
#        self.messages[0] = '''\
#            Memorize the following images and
#            their location on screen.
#            Press space to start.\
#                                '''.format()
#
#        self.messages[1] = '''\
#            A series of {x} images will appear.
#            Indicate if shown image corresponds to a previously seen image
#            and in which quadrant it has appeared earlier.
#            Press SPACE to start\
#                             '''.format(x=self.nstim+1)
#
#        self.messages[2] = '''\
#            Have you seen this picture before?
#            If yes, press "y". If not, press "n".\
#                         '''.format()
#
#        self.messages[3] = '''\
#            Where have you seen it?
#            Press 0, 1, 2 or 3 to answer\
#                         '''.format()
#
#        self.messages[4] = '''\
#            Where have you seen it?
#            0 = upper-left, 1 = upper-right
#            2 = lower-left, 3 = lower-right\
#                           '''.format()
#
#        self.messages[5] = 'Answer saved!'
#
#        self.messages[6] = 'Thank you for your time, goodbye!'
#
#    def ams_score(self):
#        '''Calculates the Amnestic Memory Score for a participant'''
#        anslist = self.trialdict['Answers']
#        good = anslist.count('recogOKposOK')
#        wrong_source = anslist.count('recogOKposWrong')
#        false_alarm = anslist.count('falseAlarm')
#        denum = (wrong_source + false_alarm)
#        if denum != 0:
#            amscore = good /(wrong_source + false_alarm)
#        else:
#            amscore = good
#        return amscore
#
#    def get_targ_pos(self, stimname, whichtrial):
#        '''
#        Returns a the position of target stimuli
#        (during encoding phase) as a tuple.
#        '''
#        for encstim in range(len(self.encstimlist[whichtrial])):
#            if stimname in self.encstimlist[encstim][0]:
#                pos = self.encstimlist[encstim][1]
#            else:
#                pos = 'None'
#            return pos
#
#    def get_answers(self, whichtrial):
#        '''
#        Returns the answers based on keys pressed by subject
#        in a list and adds this list as 'Answers' in 'self.trialdict'.
#        '''
#        answerlist = []
#        trialrecstims = self.trialdict['recStims']
#        recog = self.trialdict['Recognition']
#        pos_ans = self.trialdict['Stimpos_ans']
#        for stim in enumerate(trialrecstims):
#            shownstimname = trialrecstims[stim]
#            shownstimpos = self.get_targ_pos(trialrecstims[stim])
#            shownstim = (shownstimname, shownstimpos)
#
#            for encstim in self.encstimlist[whichtrial]:
#                if shownstim == encstim:
#                    if 'y' in recog[stim] and pos_ans[stim] == shownstim[1]:
#                        answerlist.append('recogOKposOK')
#                    elif pos_ans[stim] != shownstim[1]:
#                        answerlist.append('recogOKposWrong')
#                    elif 'n' in recog[stim]:
#                        answerlist.append('Miss')
#                elif shownstim != encstim and 'y' in recog[stim]:
#                    answerlist.append('falseAlarm')
#                else:
#                    answerlist.append('rejectOK')
#        self.trialdict.update({'Answers':answerlist})
#
#    def run_task(self, win, whichtrial):
#        '''
#        Launches the memory task. Saves each trial's dictionary
#        to 'self.outputlist'.
#        '''
#        win = visual.Window(size=(1000, 1000),
#                            color=(0, 0, 0),
#                            units='pix')
#        self.enctask = self.run_enc()
#        self.rectask = self.run_rec()
#        self.get_answers()
#        win.close()
#        return self.trialdict
#
#    def run_enc(self, win, whichtrial):
#        '''
#        Launches encoding phase.
#        A series of 'self.nstim'+1 stimuli
#        ('self.nstim' images + 1 control stimulus (gray square))
#        is shown to subject.
#        Each images appears in a quadrant on screen. Subject must
#        memorize ach image and its position (excepting control stimuli).
#
#        '''
#        self.encstimlist = []
#        thisenctrial = self.encstims[whichtrial]
#        visual.TextStim(win, text=self.messages[0]).draw()
#        win.flip()
#        event.waitKeys(keyList=["space"])
#        for stim in enumerate(thisenctrial):
#            encstim = visual.ImageStim(win, thisenctrial[stim],
#                                       color=(1, 1, 1), pos=setstimpos(),
#                                       size=(500, 500),
#                                       name=thisenctrial[stim])
#            encstim.draw()
#            win.flip()
#            encstimtuple = (encstim.name, tuple(encstim.pos))
#
#            self.encstimlist.append(encstimtuple)
#            core.wait(1)
#
#        self.stim_df = pd.DataFrame(self.encstimlist,
#                                    columns=['encStims', 'encPos'])
#        self.stimdict = self.stim_df.to_dict(orient="dict")
#        return self.encstimlist
#
#    def run_rec(self, win, whichtrial):
#        '''
#        Launches Recall phase
#
#        A series of 'self.nstim' +1 images ('self.nstim' new
#        images + 1 target image seen during encoding phase)
#        is presented to subject.
#        Subject must answer if image shown was seen or not
#        during encoding phase. If so, user must indicate at
#        which position it previously appeared (0,1,2,3).
#
#        Answers and stimuli used are returned in a dictionary.
#        All info about each run is stored in a dictionary.
#        '''
#        thisrectrial = self.recstims[whichtrial]
#        stimnamelist = []
#        reckeylist = []
#        stimpos_ans = []
#        visual.TextStim(win, text=self.messages[1]).draw()
#        win.flip()
#        pos_ans_key= []
#        event.waitKeys(keyList=["space"])
#
#        for stim in enumerate(thisrectrial):
#            stimulus = visual.ImageStim(win,
#                                        thisrectrial[stim], color=(1, 1, 1),
#                                        pos=(0.0, 0.0), size=(500, 500),
#                                        name=thisrectrial[stim])
#            visual.TextStim(win, text=self.messages[2],
#                            pos=(0.0, 300)).draw()
#            visual.TextStim(win, text=self.messages[2],
#                            pos=(0.0, 300)).autoDraw = True
#            stimulus.draw()
#            win.flip()
#            reckeys = event.waitKeys(keyList=['y', 'n'])
#            if 'y' in reckeys:
#                visual.TextStim(win, text=self.messages[4],
#                                pos=(0.0, -300)).draw()
#                win.flip()
#                poskeys = event.waitKeys(keyList=['0', '1', '2', '3'])
#                pos_ans_key.append(poskeys)
#                core.wait(1)
#            elif 'n' in reckeys:
#                pos_ans_key.append('None')
#            poskeylist = flatten(pos_ans_key)
#            reckeylist.append(reckeys)
#            if stimulus.name in self.encstimlist:
#                stimnamelist.append(stimulus.name,
#                                    self.encstimlist[stimulus.name][1])
#            else:
#                stimnamelist.append((stimulus.name, 'None'))
#            visual.TextStim(win, text=self.messages[5]).draw()
#            win.flip()
#            core.wait(1)
#
#        for poskey in enumerate(poskeylist):
#            answer = poskeylist[poskey]
#            if answer != 'None':
#                stimpos_ans.append(self.stimpos[answer])
#            elif answer == 'None':
#                stimpos_ans.append('None')
#
#        self.trialdict = {'recStims':stimnamelist,
#                          'Recognition':flatten(reckeylist),
#                          'Poskeylist':poskeylist,
#                          'Stimpos_ans':stimpos_ans,
#                          'EncStims':self.encstimlist}
#        visual.TextStim(win, text=self.messages[6]).draw()
#        win.flip()
#        core.wait(2)
#        return self.trialdict
#
task01 = ImageTask(4,2)
stimdict = task01.loadstims()
#ans = task01.outputlist
#score01 = task01.AMScore()
