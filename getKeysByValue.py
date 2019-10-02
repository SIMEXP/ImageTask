# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:34:30 2019

@author: Francois
"""

def getKeysByValues(dictOfElements, listOfValues):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] in listOfValues:
            listOfKeys.append(item[0])
    return  listOfKeys 

