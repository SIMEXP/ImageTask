# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:53:30 2019

@author: Francois
"""

from secrets import randbelow as rb

def randSign():#randomly generates 1 or -1 (quadrant position)
    if rb(2) == 0:
        return 1
    else:
        return -1 