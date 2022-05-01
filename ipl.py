# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# %%
# Loading/ Importing Dataset
batdataset = pd.read_csv('datasets/all_season_batting_card.csv')
balldataset = pd.read_csv('datasets/all_season_bowling_card.csv')
all_matches = pd.read_csv('datasets/all_season_summary.csv')

# %%
### View Batting Dataset (First 10)
print(batdataset.head(10))

#%%
### View Balling Dataset (First 10)
print(balldataset.head(10))

# %%
# Selecting Required Columns To Create New Cleaned Dataset
null1 = batdataset.isna().sum()
print(null1)

# %%
# Deleting Unwanted Columns From Batting Dataset
del batdataset['commentary']
del batdataset['runningOver']

# %%
# Fetching and Dropping NULL Valued Rows if any From Batting Dataset
null1 = batdataset.isna().sum()
print(null1)
cleaned_bat = batdataset.dropna()
print(cleaned_bat.head())
cleaned_bat.to_csv('cleaned_bat.csv')
# %%
# Verifying Null Values In Cleaned Data
null1 = cleaned_bat.isna().sum()
print(null1)

# %%
# Null Values Detection in balling dataset
null2 = balldataset.isna().sum()
print(null2)

# %%
# Deleting Unwanted Columns From Batting Dataset
del balldataset['href']

# %%
# Fetching and Dropping NULL Valued Rows if any From Batting Dataset
null1 = balldataset.isna().sum()
print(null1)
cleaned_ball = balldataset.dropna()
print(cleaned_ball.head())
cleaned_ball.to_csv('cleaned_ball.csv')
# %%
# Verifying Null Values In Cleaned Data
null1 = cleaned_ball.isna().sum()
print(null1)

# %%
# Total Matches Palayes In IPL From 2008-2021
str1 = "Total Matches Played From IPL 2008 to 2021 are: "
str2 = all_matches.shape[0]
print(str1 + str(str2))

# %%
# Visualizing Season Wise Matches Played

data = cleaned_bat.groupby(['match_id', 'season']).count().index.droplevel(level=0).value_counts().sort_index()
x = data
y = data.index
# Figure Size
fig, ax = plt.subplots(figsize=(25, 10))
plt.bar(y, x, color='#00F3D0', width=0.5)
plt.title("Season-Wise No Of Matches Played")
plt.ylabel('Season')
plt.xlabel('Matches Played')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
# Visualizing No Of Matches Played In Particular Stadiums

data = cleaned_bat.groupby(['match_id', 'venue']).count().index.droplevel(level=0).value_counts().sort_values()
x = data
y = data.index
# Figure Size
fig, ax = plt.subplots(figsize=(12, 20))
plt.barh(y, x, color='#00F3D0')
plt.title("No Of Matches Played In Particular Stadiums")
plt.ylabel('Venue/ Stadium Names')
plt.xlabel('Total Matches Played')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# %%
# Top 10 Man Of The Match Winners Of All Time IPL
t5motm = all_matches['pom'].value_counts()[:10].sort_values(ascending=False)
x = t5motm
y = t5motm.index
# Figure Size
fig, ax = plt.subplots(figsize=(16, 9))
plt.bar(y, x, color='#00F3D0')
plt.title("All Time Top 10 Man Of The Match Winners Of IPL 2008-21")
plt.ylabel('Man Of The Match Counts')
plt.xlabel('Player Names')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
all_matches['Year'] = all_matches['season']
all_matches['winner'].value_counts()[:5].sort_values()

plt.figure(figsize=(16, 9))
ax = sns.countplot(x='winner', data=all_matches, order=all_matches['winner'].value_counts()[:8].index)

plt.title("Matches Won By Particular IPL TEAMS")
plt.ylabel('Match Win Count')
plt.xlabel('Team Names')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
# Figure Size
fig, ax = plt.subplots(figsize=(16, 9))
data = cleaned_bat.groupby(['fullName'])['runs'].sum().sort_values(ascending=False)[:10]
x = data
y = data.index
plt.title("Runs Scored By Individual Players")
plt.bar(y, x, color='#00F3D0')
plt.xlabel('Batsman')
plt.ylabel('Runs')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
# Figure Size
fig, ax = plt.subplots(figsize=(16, 9))
data = cleaned_bat.groupby(['fullName'])['fours'].sum().sort_values(ascending=False)[:10]
x = data
y = data.index
plt.title("Fours Hitted By Individual Players")
plt.bar(y, x, color='#00F3D0')
plt.ylabel('Batsman')
plt.xlabel('Fours')
for bars in ax.containers:
    ax.bar_label(bars)

# %%
# Figure Size
fig, ax = plt.subplots(figsize=(16, 9))
data1 = cleaned_bat.groupby(['fullName'])['sixes'].sum().sort_values(ascending=False)[:10]
x = data1
y = data1.index
plt.title("Sixes Hitted By Individual Players")
plt.bar(y, x, color='#00F3D0')
plt.ylabel('Batsman')
plt.xlabel('Sixes')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
# Season-Wise Orange Cap Holder Scores
fig, ax = plt.subplots(figsize=(16, 9))
data2 = cleaned_bat.groupby(['season', 'fullName'])['runs'].sum().groupby('season').max()
x = data2
y = data2.index
plt.title("Orange Cap Holder Runs Count")
plt.bar(y, x, color='#00F3D0')
plt.ylabel('Max Runs By A Player')
plt.xlabel('IPL Seasons')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
# Season-Wise Purple Cap Holder Wickets
fig, ax = plt.subplots(figsize=(16, 9))
data2 = cleaned_ball.groupby(['season', 'fullName'])['wickets'].sum().groupby('season').max()
x = data2
y = data2.index
plt.title("Purple Cap Holder Wickets Count")
plt.bar(y, x, color='#00F3D0')
plt.ylabel('Max Wickets By A Player')
plt.xlabel('IPL Seasons')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
# All Time Wickets Taken By Individual Players
fig, ax = plt.subplots(figsize=(16, 9))
data = cleaned_ball.groupby(['fullName'])['wickets'].sum().sort_values(ascending=False)[:5]
x = data
y = data.index
plt.title("Wickets Taken By Individual Players")
plt.bar(y, x, color='#00F3D0')
plt.xlabel('Bowler Names')
plt.ylabel('Wickets')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
# All Time Maiden Overs By Individual Players
fig, ax = plt.subplots(figsize=(16, 9))
data = cleaned_ball.groupby(['fullName'])['maidens'].sum().sort_values(ascending=False)[:5]
x = data
y = data.index
plt.title("All Time Maiden Overs By Individual Players")
plt.bar(y, x, color='#00F3D0')
plt.xlabel('Bowler Names')
plt.ylabel('Maidens Count')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# %%
# All Time No Balls By Individual Players
fig, ax = plt.subplots(figsize=(16, 9))
data = cleaned_ball.groupby(['fullName'])['noballs'].sum().sort_values(ascending=False)[:5]
x = data
y = data.index
plt.title("All Time No Balls By Individual Players")
plt.bar(y, x, color='#00F3D0')
plt.xlabel('Bowler Names')
plt.ylabel('No Balls Count')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()
