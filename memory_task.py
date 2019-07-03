#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#MEMORY TASK (BETA)
from __future__ import division
import os
from PIL import Image
import random
from psychopy import core, visual, event #help(visual.ImageStim)

win = visual.Window(size=(1000, 1000), color=(0, 0 , 0), units = 'pix')

imPaths = []#Lists all images full paths
faceCounter = 1
for r, d, f in os.walk('/home/fnadeau/Pictures/face_human'):
    for file in f:
        if '.jpg' in file:
            imPaths.append(os.path.join(r, file))
            faceCounter += 1           

def randSign():#randomly generates 1 or -1 (quadrant position)
    if random.random() < 0.5:
        return 1
    else:
        return -1

# SIMA-Q does perfect balancing
# Image task images shouldn't be redrawn except for few targets
nStim = 10
stimCounter = 1
stimList = []#List of stimuli used in order with quadrant position for a trial
key_pressed = []
imageSelection = []
imageCounter = 1
for item in imPaths:
    while imageCounter <= nStim:
        imageSelection.append(imPaths[random.randint(0, len(imPaths))])
        imageCounter += 1
print(*imageSelection, sep = '\n')

while stimCounter <= nStim:
    image = visual.ImageStim(win,image=imageSelection[random.randint(0, nStim-1)],color=(1,1,1), pos = (randSign()*250, randSign()*250), size = (500, 500))
    image.draw()
    win.flip()
    core.wait(2.0)
    stimCounter += 1
    key_pressed.append(event.getKeys(keyList=[0,1,2,3], modifiers=False, timeStamped=True))
    stimList.append({'image':image.image, 'position':image.pos})
print(*stimList, sep = '\n')
win.close()

