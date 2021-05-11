# in this script we integrate all the modules to create, solve and visulize the SWF problem

#%% import modules 
import LoadModel
import RandomSolution
import ParsingSolution
#%% Load model 
model=LoadModel.SelectModel()

#%% create random solution 
randsol=RandomSolution.Create(model)

# %% parse solution 
sol=ParsingSolution.Parse(model,randsol)
# %%
