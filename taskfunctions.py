# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:06:24 2019

@author: Francois
"""
import os
import pandas as pd
from random import sample as randsmp
from secrets import randbelow as rb
from typing import Sequence

def properIndex(folderName):
    '''Names and indexes images according to category'''
    cwd = os.getcwd()
    sources = pd.read_csv(os.path.join(cwd, 'sources.csv'))
    references = sources['reference'].tolist()

    folderpath = os.path.join(cwd,folderName)

    for root, dirs, files in os.walk(folderpath):
        counter = 1
        for file in files:
            impath = os.path.join(root,file)
            dirPath = os.path.dirname(impath)
            dName = os.path.basename(dirPath)
            if 'bodypart' in dName:
                dName = dName.replace('bodypart','body_part')
            for ref in references.__iter__():
                refInd = file.find(ref)
                if refInd != -1:
                    suffix = file[refInd:]
            if counter <= 9:
                okName = dName  + '0' + str(counter) + suffix
            elif counter >= 10:
                okName = dName + str(counter) + suffix
            okPath,ext = os.path.splitext(os.path.join(root,okName))
            os.rename(impath,okPath+'.jpeg')
            counter +=1
            print(len(os.listdir(dirPath)))

def randSign():
    '''
    Randomly generates 1 or -1 (quadrant position)
    '''
    if rb(2) == 0:
        return 1
    else:
        return -1

def setstimpos():
    '''
    Randomly sets the position of stimuli durung encoding
    phase

    '''
    setpos = (randSign()*250, randSign()*250)
    return setpos

def flatten(nestedlst):
    """
    Description
    -----------
    Returns unidimensional list from nested list using list comprehension.

    Parameters
    ----------
        nestedlst: list containing other lists etc.

    Variables
    ---------
        bottomElem: type = str
        sublist: type = list

    Return
    ------
        flatlst: unidimensional list
    """
    flatlst = [bottomElem for sublist in nestedlst
              for bottomElem in (flatten(sublist)
              if (isinstance(sublist, Sequence)
              and not isinstance(sublist, str))
              else [sublist])]
    return flatlst

def loadimages(imdir='images'):
    '''
    Description
    -----------
    Lists the full relative path of all '.jpeg' files in a directory.

    Parameters
    ----------
    imdir: type = str
        Name of the directory containing the images.

    Return
    ------
    imlist: type = list
        1D list containing all '.jpeg' files' full relative paths
    '''
    imlist = []
    impath = os.path.join(os.getcwd(),imdir)
    for root, dirs, images in os.walk(impath):
        for image in images:
            if '.jpeg' in image:
                imlist.append(os.path.join(root,image))
    return imlist

def sampling(lst,nsize,nsamples,exclusives=[]):
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
    inds = randsmp(range(0, len(lst)), nsize*nsamples)#len = 640
    exclusives = flatten(exclusives)
    for item in range(len(exclusives)):
        if item in flatten(inds) and item in exclusives:
            inds.remove(item)
#    [inds.remove(exclusives[item])
#           for item in range(len(exclusives))
#           if item in flatten(inds)]
    samples = [inds[ind:ind+nsize] for ind in range(0, len(inds), nsize)]

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

def imMatrix(samples):
    nsize = len(samples[0])
    imMatrix = []
    images = loadimages()
    samples = flatten(samples)

    for item in samples:
        imMatrix.append(images[item])

    imMatrix = [imMatrix[ind:ind+nsize]
               for ind in range(0, len(imMatrix), nsize)]
    return imMatrix
#examples
#nsize,nsamples,lst = 80,8,loadimages()
#
#invalid = sampling(lst,40,8)
#estims = sampling(lst,80,8,exclusives=invalid)
#rstims = [estims[nsample]+invalid[nsample] for nsample in range(len(estims))]
#encstims,recstims = imMatrix(estims),imMatrix(rstims)

