# -*- coding: utf-8 -*-

"""

Created on Wed May  5 01:10:02 2021


@author: anadinajafabad

"""
#%%
import numpy as np 
import pandas as pd
#%%
def Parse(model,randsol):
#%%
    Z=model['Z']
    w=model['aisle_width']
    v=model['cross_aisle_width']
    S=model['S']
    g=model['g']
    h=model['h']

    l=randsol['NumberOfLevels']
    q=randsol['SequenceOfCompanies']
    n=randsol['NumberOfAisles']
    
    
    

    delimiterposition= np.where(q>Z)[0]

    From= np.concatenate(([0],delimiterposition+1),axis=0)

    To=np.concatenate((delimiterposition,[Z+l-1]),axis=0)
    
# %% decompose assignment into the levels and calculate coordinates of the areas 
    sol={}
    L={}
    X0={}
    Xend={}
    Y0={}
    Yend={}

    for j in range(l): 
        L[str(j)]=q[From[j]:To[j]]
        if len(L[str(j)])==0:
            X0[str(j)]=np.zeros(1)
            Xend[str(j)]=np.zeros(1)
            Y0[str(j)]=np.zeros(1)
            Yend[str(j)]=np.zeros(1)
        else:            
            X0[str(j)]=np.zeros(len(L[str(j)]))
            Xend[str(j)]=np.zeros(len(L[str(j)]))
            Y0[str(j)]=np.zeros(len(L[str(j)]))
            Yend[str(j)]=np.zeros(len(L[str(j)]))

        if L[str(j)].size >0:
            if L[str(j)].size ==1:
                Xend[str(j)][0]=X0[str(j)][0]+n[L[str(j)][0]-1]*w
                if j==0:
                    Yend[str(j)][0]=Y0[str(j)][0]+(S/(n[L[str(j)][0]-1])+(2*v))
                else:
                    Y0[str(j)][0]=min(Yend[str(j-1)])
                    Yend[str(j)][0]=Y0[str(j)][0]+(S/(n[L[str(j)][0]-1])+(2*v))  
            else:
                for k in range(len(L[str(j)])-1):
                    X0[str(j)][k+1]=X0[str(j)][k]+n[L[str(j)][k]-1]*w
                    Xend[str(j)][k]=X0[str(j)][k]+n[L[str(j)][k]-1]*w
                    if j==0:
                        Yend[str(j)][k]=Y0[str(j)][k]+(S/(n[L[str(j)][k]-1])+(2*v))

                        if k ==len(L[str(j)])-2:
                            Xend[str(j)][k+1]=X0[str(j)][k+1]+n[L[str(j)][k+1]-1]*w                     
                            Yend[str(j)][k+1]=Y0[str(j)][k+1]+(S/(n[L[str(j)][k+1]-1])+(2*v))
                    else:
                        Y0[str(j)][k]=min(Yend[str(j-1)])
                        Yend[str(j)][k]=Y0[str(j)][k]+(S/(n[L[str(j)][k]-1])+(2*v))  

                        if k ==len(L[str(j)])-2:
                            Xend[str(j)][k+1]=X0[str(j)][k+1]+n[L[str(j)][k+1]-1]*w
                            Y0[str(j)][k+1]=min(Yend[str(j-1)])
                            Yend[str(j)][k+1]=Y0[str(j)][k+1]+(S/(n[L[str(j)][k+1]-1])+(2*v))
        else:
            if j==0:
                Yend[str(j)][0]=Y0[str(j)][0]
            else:
                Y0[str(j)][0]=min(Yend[str(j-1)])
                Yend[str(j)][0]=Y0[str(j)][0]
 # %%calculate the violation 
    sol['X0']=X0
    sol['Xend']=Xend
    sol['Y0']=Y0
    sol['Yend']=Yend
    sol['levels']=L             

                        

    return sol