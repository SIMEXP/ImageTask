# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:01:56 2019

@author: Francois
"""
from secrets import randbelow as rb

def sampling(lst,nsize,nsamples,exclusives=[],label='sample'):
    samples = list(range(nsamples))
    for nsample in range(nsamples):
        samples[nsample] = [lst[rb(len(lst))] 
                           for nsample in range(nsize)
                           if lst[rb(len(lst))] 
                           not in samples 
                           and lst[rb(len(lst))] not in exclusives]

    sampledict = {label+str(nsample):samples[nsample]
             for nsample in range(nsamples)}
    try:
        x = sampledict  
        for y in exclusives:
            shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
    except:
        len(shared_items) != 0
        print('error:non-exclusive')
    else:
        return sampledict
