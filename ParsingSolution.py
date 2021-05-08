# -*- coding: utf-8 -*-
"""
Created on Wed May  5 01:10:02 2021

@author: anadinajafabad
"""
import numpy as np 

def Parse(model,randsol):
    sol={}
    Z=model['Z']
    l=randsol['NumberOfLevels']
    q=randsol['SequenceOfCompanies']
    n=randsol['NumberOfAisles']
    
    
    delimiterposition= np.where(q>Z)[0]
    From= np.concatenate(([0],delimiterposition+1),axis=0)
    To=np.concatenate((delimiterposition,[Z+l-1]),axis=0)
    
    L={}
    for j in range(l):
        L[str(j)]=q[From[j]:To[j]]
        
        if L[str(6)].size >0:
            
            
    
    
    return sol