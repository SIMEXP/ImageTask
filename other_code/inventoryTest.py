# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 15:57:52 2019

@author: Francois
"""

import os
import pandas as pd
import sklearn
from sklearn.datasets import load_iris

iris = load_iris()

cwd = os.getcwd()
inventory = pd.read_csv(os.path.join(cwd,'inventory_inanimate.csv'))
synsets = inventory['synset'].tolist()
from brisque import BRISQUE