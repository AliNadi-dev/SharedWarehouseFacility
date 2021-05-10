# -*- coding: utf-8 -*-
"""
Created on Tue May  4 01:37:48 2021

@author: anadinajafabad
"""
import random
import numpy as np 

def Create(model):
    Z=model['Z']
    S=model['S']
    minlevel=1              # minimum number of levels
    maxlevel=round(Z/2)     # maximum number of levels
    nmin=1                  # minimum number of aisles
    nmax=S/10               # maximum number of aisles assuming the minimum length of aisles is 10 m
    numberofLevels=random.randint(minlevel,maxlevel)
    numberofAisles=[random.randint(nmin,nmax) for i in range(Z)]
    randsol={}
    randsol['NumberOfLevels']=numberofLevels
    randsol['NumberOfAisles']=numberofAisles
    randsol['SequenceOfCompanies']=np.random.permutation(Z+numberofLevels-1)+1
    
    return randsol