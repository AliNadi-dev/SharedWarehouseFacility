# -*- coding: utf-8 -*-
"""
Created on Tue May  4 00:23:18 2021

@author: anadinajafabad
"""
from  CreateModels import CreateInstance
import pickle
#%%
def SaveInstances():
    W=[300,600]
    Z=[10,15,20]
    Lambda1=[50,50,50]
    Lambda2=[50,75,100] 
    for i in range(len(W)):
        for j in range(len(Z)):
            model=CreateInstance(W[i],Z[j],Lambda1[j])            
            file_name='model_'+ str(W[i]) + '_' + str(Z[j]) + '_' + str(Lambda1[j])+'.pkl'
            f = open(file_name,"wb")
            pickle.dump(model,f)
            f.close()
            model2=CreateInstance(W[i],Z[j],Lambda2[j])            
            file_name='model_'+ str(W[i]) + '_' + str(Z[j]) + '_' + str(Lambda2[j])+'.pkl'
            f = open(file_name,"wb")
            pickle.dump(model2,f)
            f.close()           
    return    



