# -*- coding: utf-8 -*-
"""
Created on Tue May  4 01:03:14 2021

@author: anadinajafabad
"""

import easygui
import pickle
#%%

def SelectModel():
    path=easygui.fileopenbox(default='*.pkl')
    
    if str(type(path))=="<class 'str'>":
        infile = open(path,'rb')
        model = pickle.load(infile)
        infile.close()
    else:
        model={}
    return model