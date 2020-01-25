
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:36:21 2019

@author: Francois
"""
import csv
from os.path import basename as bname
from random import randint
from random import sample
from psychopy import core
#from psychopy import data
from psychopy import event
#from psychopy import logging
from psychopy import visual
from taskfunctions import get_answers
from taskfunctions import loadimages
from taskfunctions import sampling

CTRL_STIM_PATH = '/home/francois/GitHub/ImageTask/Solid_grey.jpg'
IMPATH = '/home/francois/Desktop/neuromod_image_bank'

class ImageTask():
    '''Runs the NeuroMod/CIMA-Q memory task
    '''
    def __init__(self, nstim, nrun, impath, ctrlstim):
        '''
        Parameter(s)
        ----------
        nrun: Number of runs for a subject
        nstim: Number of new images used in each phase in a run
        impath: Path to images folder
        ctrlstimpath: Path to control stimuli
        stimdict: Dictionary containing stimuli lists for each run (key)
                  in both encoding & retrieval conditions (values) a given
                  participant will do
                  (i.e. stimdict[whichrun][0] = stim names for enc. phase*;
                        *includes distractor (gray square) stimuli
                        stimdict[whichrun][1] = stim names for rec. phase)
        '''
        self.nstim = nstim
        self.nrun = nrun
        self.impath = impath
        self.ctrlstim = ctrlstim
        self.stimdict = self.loadstims(impath)
        self.stimpos = {'1':(-250.0, 250.0),
                        '2':(250.0, 250.0),
                        '3':(250.0, -250.0),
                        '4':(-250.0, -250.0)}
    def loadstims(self, impath):
        '''
        Description
        -----------
        Creates lists of nstim stimuli (encoding)
        & nstim+nstim/2 stimuli (recall)
        Distractor stimuli are exclusive of encoding stimuli & come from
        the same semantic categories.
        Control stimuli (gray squares) are added to encoding list during
        'runEnc' execution.

        Parameter(s)
        ------------
        impath: String or path-like object pointing to image bank location

        Returns
        -------
        stimdict: Dictionary containig a participant's images for every
        run (encoding & recall conditions). Easy to save to CSV or similar
        format.
        '''
        allpics = loadimages(impath)
        # Selecting exclusive distractor stimuli
        invld = sampling(allpics, int(self.nstim/2), self.nrun)
        # Selecting encoding stimuli
        encstims = sampling(allpics, int(self.nstim), self.nrun,
                            exclusives=[invld])
        # Combining encoding+distractor images into recall stimuli lists
        recstims = [sample(encstims[nrun]+invld[nrun],
                            len(encstims[0])+len(invld[0]))
                    for nrun in range(len(encstims))]
        # Adding control stimuli (gray square) to encoding stimuli lists
        for run in range(self.nrun):
            encstims[run] = sample(encstims[run]+int(self.nstim/2)*['GS'],
                                    int(self.nstim*1.5))
        # Stimuli dict: keys = runs, values = encstims[run], recstims[run]
        stimdict = dict(zip([nrun for nrun in range(self.nrun)],
                            [[encstims[nrun], recstims[nrun]]
                             for nrun in range(self.nrun)]))
        # Replace stimuli indices for their respective paths
        for values in stimdict.values():
            for stimsets in values:
                for pic_ind in stimsets:
                    if pic_ind != 'GS':
                        stimsets[stimsets.index(pic_ind)] = allpics[pic_ind]
                    else:
                        stimsets[stimsets.index(pic_ind)] = self.ctrlstim
        # Saving to csv for future uses
        with open('dict.csv', 'w', newline="") as csv_file:
            writer = csv.writer(csv_file)
            for key, value in stimdict.items():
                writer.writerow([key, value])
        return stimdict

    def run_task(self, whichrun):
        '''
        Description
        -----------
        Launches the memory task (encoding followed by recall phases).
        Saves every stimuli for both phases (stimulus name & position) in a
        dictionary for each run. A run consists in a full encoding then
        retrieval cycle.

        Parameter(s)
        ------------
        whichrun: Integer specifying which run

        Returns
        -------
        rundict: Dictionary containing
                   A) Stimuli info (name & position) for encoding condition
                   B) Stimuli info for (name & answer) for recall condition
                   C) Results for each answer (HIT, FA, MISS, CR)
        '''
        messages = list(range(7))

        messages[0] = '''
        Memorize the following images & their location on screen.
        Press space to start.'''

        messages[1] = '''A series of {x} images will appear.
        Indicate if shown image corresponds to a previously
        seen image and in which quadrant it has appeared earlier.
        Press SPACE to start'''.format(x=self.nstim+int(self.nstim/2))

        messages[2] = '''
        Have you seen it earlier?
        Press "y" for yes, "n" for no.'''.format()

        messages[3] = '''
        Where have you seen it?
        Press 0, 1, 2 or 3 to answer'''.format()

        messages[4] = '''
        Where have you seen it?
        1 = upper-left, 2 = upper-right
        3 = lower-left, 4 = lower-right'''.format()

        messages[5] = 'Answer saved!'

        messages[6] = 'Thank you for your time, goodbye!'

        win = visual.Window(size=(1000, 1000),
                            color=(-1.0, -1.0, -1.0),
                            units='pix')
        encstimlist = self.run_enc(win, whichrun, messages)
        recall = self.run_rec(win, whichrun, messages, encstimlist)
        win.close()
        return recall

    def run_enc(self, win, whichrun, messages):
        '''
        Launches encoding phase.
        A series of 'self.nstim'+1 stimuli
        ('self.nstim' images + 1 control stimulus (gray square))
        is shown to subject.
        Each images appears in a quadrant on screen. Subject must
        memorize ach image and its position (excepting control stimuli).
        '''
        encstimlist = []
        thisencrun = list(self.stimdict[whichrun][0])
        thisencrun = sample(thisencrun, len(thisencrun))
        visual.TextStim(win, text=messages[0], pos=(250.0, 0.0)).draw()
        win.flip()
        event.waitKeys(keyList=["space"])
        for stim in enumerate(thisencrun):
            encstim = visual.ImageStim(win, stim[1],
                                       color=(1, 1, 1),
                                       pos=self.stimpos[str(randint(1, 4))],
                                       size=(500, 500),
                                       name=bname(stim[1]))
            encstim.draw()
            win.flip()
            encstimtuple = (encstim.name, tuple(encstim.pos))
            encstimlist.append(encstimtuple)
            core.wait(1)
        return encstimlist

    def run_rec(self, win, whichrun, messages, encstimlist):
        '''
        Launches Recall phase

        A series of 'self.nstim' images ('self.nstim' new
        images + 'self.nstim'/2 target image seen during encoding phase)
        is presented to subject.
        Subject must answer if image shown was seen or not
        during encoding phase. If so, user must indicate at
        which position it previously appeared (1,2,3 or 4).

        Answers and stimuli used are returned in a dictionary.
        All info about each run is stored in a dictionary.
        '''
        thisrecrun = self.stimdict[whichrun][1]
        stimnamelist = []
        visual.TextStim(win, text=messages[1], pos=(250.0, 0.0)).draw()
        win.flip()
        event.waitKeys(keyList=["space"])
        for stim in enumerate(thisrecrun):
            stimulus = visual.ImageStim(win,
                                        stim[1], color=(1, 1, 1),
                                        pos=(0.0, 0.0), size=(500, 500),
                                        name=bname(stim[1]))
            visual.TextStim(win, text=messages[2],
                            pos=(250.0, 300)).draw()
            visual.TextStim(win, text=messages[2],
                            pos=(250.0, 300)).autoDraw = True
            stimulus.draw()
            win.flip()
            reckeys = event.waitKeys(keyList=['y', 'n'])
            if 'y' in reckeys:
                visual.TextStim(win, text=messages[4],
                                pos=(250.0, -300)).draw()
                win.flip()
                poskeys = event.waitKeys(keyList=['1', '2', '3', '4'])
                stimnamelist.append((stimulus.name,
                                     self.stimpos[str(poskeys[0])]))
                core.wait(1)
            elif 'n' in reckeys:
                stimnamelist.append((stimulus.name, 'None'))
            visual.TextStim(win, text=messages[5]).draw()
            win.flip()
            core.wait(1)
        rundict = {'recstims':stimnamelist, 'encstims':encstimlist}
        get_answers(rundict)
        visual.TextStim(win, text=messages[6]).draw()
        win.flip()
        core.wait(2)
        return rundict

task01 = ImageTask(4, 20, impath=IMPATH, ctrlstim=CTRL_STIM_PATH)
# To see what a participant's stimuli list for all runs looks like
stimdict_test = task01.loadstims(IMPATH)
this_run = task01.run_task(0) #Run number 0
