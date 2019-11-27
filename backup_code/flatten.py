# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 00:28:09 2019

@author: Francois
"""
from typing import Sequence

def flatten(nestedlst):
    """ Returns unidimensional list from nested list
        using list comprehension
    Parameters:
        nestedlst: list containing other lists etc.
    -----------------------------------------------
    Variables:
        bottomElem: type = str
        sublist: type = list
    --------------------------
    Return:
        flatlst: unidimensional list
        """
    flatlst = [bottomElem for sublist in nestedlst 
              for bottomElem in (flatten(sublist) 
              if (isinstance(sublist, Sequence) 
              and not isinstance(sublist, str)) 
              else [sublist])]
    return flatlst