# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 06:42:24 2019

@author: Francois
"""

import numpy as np
import os
from random import randrange
from random import sample
from secrets import choice
from secrets import randbelow as rb
from taskfunctions import flatten
from typing import Sequence

def sampling(lst,nsize,nsamples,exclusives=[],output='dict',label='sample'):
    '''
    Description
    -----------
    Draws desired amount of samples of desired size without
    replacement from population.
    Output can be either list or dict.
    
    Parameters
    ----------
    lst: type=list
        Input list from where population elements are sampled.
    
    nsize: type=int
        Size of each sample.
    
    nsamples: type=int
        Number of samples to be drawn from 'lst'
    
    exclusives: type=list or type=dict
    '''
    
    samples = list(range(nsamples))#len=16
    inds = sample(range(0, len(lst)), nsize*nsamples)#len = 1280
    exclusives = flatten(exclusives)
    [inds.remove(exclusives[exc]) for exc in range(len(exclusives)) if exclusives[exc] in inds]
    len(inds)
#    exclusives = flatten([flatten(exclusives[exc]) for exc in range(len(exclusives))])
    samples = [inds[ind:ind+nsize] for ind in range(0, len(inds), nsize)]

    
#    samples = [inds[int(sInds[nsample]):int(sInds[nsample+1])]
#              for nsample in range(len(samples)-1)]

    try:
        for exclusive in exclusives:
            errorMsg = 'non-exlusive samples'
            shared_items = []
            for item in flatten(samples):
                if item in flatten(exclusive):
                    shared_items.append(item)
        len(shared_items) != 0
        print(errorMsg)
        
    except:
        return samples

nsize,nsamples,lst = 80,8,loadimages()
distractors = sampling(lst,40,nsamples)
exclusives = distractors
encstims = sampling(lst,80,nsamples,exclusives=distractors)
#encstims = np.array(encstims)