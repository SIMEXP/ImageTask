# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:30:07 2019

@author: Francois
"""
from secrets import randbelow as rb
from flatten import flatten

def randInsert(lst, item):
    """Insert element to random index in list
    Parameters:
        lst: list object
        item: any type variable
    ---------------------------
    Variables:
        sliceIndex: type = int
        lstTop, lstBottom: type = list
    ----------------------------------
    Return:
        newlst: unidimensional list 
    """
    sliceIndex = rb(len(lst)-1)# type = int
    lstTop, lstBottom = lst[:sliceIndex], lst[sliceIndex:]
    lstTop.append(item)
    lstTop.append(lstBottom)
    newlst = flatten(lstTop)
    return newlst