#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
#%%
# Loading/ Importing Dataset
batdataset = pd.read_csv('datasets/all_season_batting_card.csv')
balldataset = pd.read_csv('datasets/all_season_bowling_card.csv')
#%%
# Printing Batting Dataset
print(batdataset.head())
#%%
# Printing Balling Dataset
print(balldataset.head())

#%%
# Selecting Required Columns To Create New Cleaned Dataset
null1 = batdataset.isna().sum()
print(null1)
#%%
# Deleting Unwanted Columns From Batting Dataset
del batdataset['commentary']
del batdataset['runningOver']
#%%
# Fetching and Dropping NULL Valued Rows if any From Batting Dataset
null1 = batdataset.isna().sum()
print(null1)
cleaned_bat = batdataset.dropna()
print(cleaned_bat.head())

#%%
# Verifying Null Values In Cleaned Data
null1 = cleaned_bat.isna().sum()
print(null1)


#%%
# Null Values Detection in balling dataset
null2 = balldataset.isna().sum()
print(null2)
#%%
# Deleting Unwanted Columns From Batting Dataset
del balldataset['href']

#%%
# Fetching and Dropping NULL Valued Rows if any From Batting Dataset
null1 = balldataset.isna().sum()
print(null1)
cleaned_ball = balldataset.dropna()
print(cleaned_ball.head())

#%%
# Verifying Null Values In Cleaned Data
null1 = cleaned_ball.isna().sum()
print(null1)

#%% Visualizing Batting Data
#
x = cleaned_bat['fullName']
y = cleaned_bat['ballsFaced']
plt.bar(x, y)
plt.show()


#%%
# Visualizing Balling Data

