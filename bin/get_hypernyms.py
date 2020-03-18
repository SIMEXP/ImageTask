#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:00:08 2020

@author: francois
"""

from itertools import chain
import pandas as pd
import os
from nltk.corpus import wordnet as wn

def get_hypernyms(wordlist):
    wordlist = pd.read_csv(os.path.join(os.getcwd(),wordlist))
    second_hypernyms = {}
    for concept in wordlist["1_hypernym"]:
        concept_path = wn.synset(concept).hypernym_paths()[0]
        for synset in enumerate(concept_path):
            concept_path[synset] = synset[1].name()
            second_hypernyms[concept] = concept_path
#        for word in enumerate(second_hypernyms[concept]):
#            word = word[1].name()
        return second_hypernyms
#        for synset in concept_hypernym_paths:
#            synset = synset.name()
#            
#        print(concept_hypernym_paths)

#        for idx, path in enumerate(concept_hypernym_paths):
#            for synset in path:
#                 second_hypernyms[concept].append(synset.name())
#        
#    return second_hypernyms
##
second_hypernyms = get_hypernyms("hypernyms.csv")
##from nltk.corpus import wordnet as wn
# 
#input_word = raw_input("Enter word to get hyponyms and hypernyms: ")
# 
#for i,j in enumerate(wn.synsets(concept)):
#print "Meaning",i, "NLTK ID:", j.name()
#print "Hypernyms:", ", ".join(list(chain(*[l.lemma_names() for l in j.hypernyms()])))
#print "Hyponyms:", ", ".join(list(chain(*[l.lemma_names() for l in j.hyponyms()])))
#print
for word in enumerate(surgeonfish):
    print(word[1].name())