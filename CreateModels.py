# -*- coding: utf-8 -*-
"""
Created on Mon May  3 01:31:50 2021

@author: anadinajafabad
"""
import numpy as np
import pandas as pd

#%% shared warehouse facility and layout design 


def CreateInstance(W,Z,Lambda):
    
    model={}
    S=150                           # required aisle length
    w=3                             # aisle width
    v=3                             # Cross aisle width
    M=50                            # maximum number of items per picking routes
    alpha=50                        # maximum number of orders that can be satisfied 
                                    # from one pallet
    
    N=15                            # max number of aisle                        
     
                             
    xmin=0  
    xmax=W
    
    ymin=0
    ymax=[]                          # Depth of warehous is unknown
    
    g = pd.read_excel("data.xlsx", sheet_name='g')
    h = pd.read_excel("data.xlsx", sheet_name='h')
    
    
    model['Orders']={}
    for i in range(1,Z+1):
        model['Orders'][str(i)]=np.random.randint(1,M+1,Lambda)

    
    model['Width']=W   # width of warehouse 
    model['Z']=Z   # number of companies 
    model['Lambda']=Lambda  # average number of orders per day
    
    model['Depth']=[]
    model['aisle_width']=w  
    model['cross_aisle_width']=v
    model['N']=N
    model['alpha']= alpha 
    model['M']= M 
    model['S']= S
    model['xmin']=xmin   
    model['ymin']=ymin
    model['xmax']=xmax
    model['ymax']=ymax
    model['g']=g
    model['h']=h
    
    return model