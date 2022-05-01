#  Data Visualization Project
## **Description**
	

## **Requirements**
	1. VS CODE/ PyCharm/ DataSpell/ Jupyter or any other Python Supported IDE.
	2. Python Version 3+ Installed (Install Python Packages - NUMPY, PANDAS, MATPLOTLIB)
	3. LINUX/ WINDOWS/ MAC OS SYSTEM
	4. Github Knowledge

## **INDEX**
### Data Preprocessing (Dataset Link: <a href="https://www.kaggle.com/datasets/rajsengo/indian-premier-league-ipl-all-seasons">Click Here</a>)
    1. Data Loading
    2. Data Cleaning
    3. 
    4. 
    5. 

#### Import Packages
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from collections import Counter

#### Loading/ Importing Dataset
    batdataset = pd.read_csv('datasets/all_season_batting_card.csv')
    balldataset = pd.read_csv('datasets/all_season_bowling_card.csv')
    all_matches = pd.read_csv('datasets/all_season_summary.csv')

#### View Batting Dataset (First 10)
    print(batdataset.head(10))

#### Selecting Required Columns To Create New Cleaned Battiing Dataset
    null1 = batdataset.isna().sum()
    print(null1)

    # -- Deleting Unwanted Columns From Batting Dataset --
    del batdataset['commentary']
    del batdataset['runningOver']

    # Fetching and Dropping NULL Valued Rows if any From Batting Dataset
    null1 = batdataset.isna().sum()
    print(null1)
    cleaned_bat = batdataset.dropna()
    print(cleaned_bat.head())
    cleaned_bat.to_csv('cleaned_bat.csv')

    # Verifying Null Values In Cleaned Data
    null2 = cleaned_bat.isna().sum()
    print(null2)

#### View Balling Dataset (First 10)
    print(balldataset.head(10))

#### Selecting Required Columns To Create New Cleaned Balling Dataset
    # Null Values Detection in balling dataset
    null2 = balldataset.isna().sum()
    print(null2)

    #Deleting Unwanted Columns From Batting Dataset
    del balldataset['href']
    
    # Fetching and Dropping NULL Valued Rows if any From Balling Dataset
    null1 = balldataset.isna().sum()
    print(null1)
    cleaned_ball = balldataset.dropna()
    print(cleaned_ball.head())
    cleaned_ball.to_csv('cleaned_ball.csv')
    
    # Verifying Null Values In Cleaned Data
    null2 = cleaned_ball.isna().sum()
    print(null2)

####
    # Setting Colors
    cmix = ["#00FFFF", "#F0FFFF", "#89CFF0", "#0000FF", "#7393B3", "#088F8F", "#0096FF", "#5F9EA0","#0047AB", "#6495ED",	"#00FFFF",	"#00008B",	"#6F8FAF",	"#1434A4",	"#7DF9FF",	"#6082B6",	"#00A36C", "#3F00FF",	"#5D3FD3",	"#ADD8E6",	"#191970",	"#000080",	"#1F51FF",	"#A7C7E7",	"#CCCCFF",	"#B6D0E2",	"#96DED1",	"#4169E1",	"#0F52BA",	"#9FE2BF",	"#87CEEB",	"#4682B4",	"#008080", "#40E0D0", "#0437F2",	"#40B5AD",	"#0818A8"]
    
    c10 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#00F3D0', '#bcbd22', '#17becf']
    
    c5 = ['#1f77b4', '#ff7f0e', '#00F3D0', '#bcbd22', '#17becf']




### List Of Visualizations Performed
#### 1. Total Matches Palayes In IPL From 2008-2021
    str1 = "Total Matches Played From IPL 2008 to 2021 are: "
    str2 = all_matches.shape[0]
    print(str1 + str(str2))   
#### 2. Season-Wise No Of Matches Played 2008-21
    # Visualizing Season Wise Matches Played
    
    data = cleaned_bat.groupby(['match_id', 'season']).count().index.droplevel(level=0).value_counts().sort_index()
    x = data
    y = data.index
    # Figure Size
    fig, ax = plt.subplots(figsize=(25, 10))
    plt.bar(y, x, color=cmix, width=0.8)
    plt.title("Season-Wise No Of Matches Played 2008-21")
    plt.xlabel('Season')
    plt.ylabel('Matches Played')
    for bars in ax.containers:
    ax.bar_label(bars)
    plt.show()
![Visualization 1](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual1.png)

    Conclusion:

    2008 - 58   |   2009 - 57   |   2010 - 60   |   2011 - 73   |   2012 - 74
    2013 - 76   |   2014 - 60   |   2015 - 59   |   2016 - 60   |   2017 - 59
    2018 - 60   |   2019 - 60   |   2020 - 60   |   2021 - 60

#### 3. Total No Of Matches Played In Particular Stadiums 2008-21
    data = cleaned_bat.groupby(['match_id', 'venue']).count().index.droplevel(level=0).value_counts().sort_values()
    x = data
    y = data.index
    # Figure Size
    fig, ax = plt.subplots(figsize=(12, 20))
    plt.barh(y, x, color=cmix)
    plt.title("No Of Matches Played In Particular Stadiums 2008-21")
    plt.ylabel('Venue/ Stadium Names')
    plt.xlabel('Total Matches Played')
    for bars in ax.containers:
    ax.bar_label(bars)
    plt.show()
![Visualization 2](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual2.png)

#### 4. Top 10 Man Of The Match Winners Of All Time IPL
    # Top 10 Man Of The Match Winners Of All Time IPL
    t5motm = all_matches['pom'].value_counts()[:10].sort_values(ascending=False)
    x = t5motm
    y = t5motm.index
    # Figure Size
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.bar(y, x, color=c10)
    plt.title("All Time Top 10 Man Of The Match Winners Of IPL 2008-21")
    plt.ylabel('No Of Times Man Of The Match Counts')
    plt.xlabel('Player Names')
    for bars in ax.containers:
    ax.bar_label(bars)
    plt.show()
![Visualization 3](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual3.png)

#### 5. No Of Total Matches Won By Particular IPL TEAMS 2008-21
    all_matches['Year'] = all_matches['season']
    all_matches['winner'].value_counts()[:5].sort_values()
    
    plt.figure(figsize=(16, 9))
    ax = sns.countplot(x='winner', data=all_matches, order=all_matches['winner'].value_counts()[:8].index)
    
    plt.title("No Of Total Matches Won By Particular IPL TEAMS 2008-21")
    plt.ylabel('Match Win Count')
    plt.xlabel('Team Names')
    for bars in ax.containers:
    ax.bar_label(bars)
    plt.show()
![Visualization 4](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual4.png)

#### 6. Total IPL Runs Scored By Individual Players 2008-21
    fig, ax = plt.subplots(figsize=(16, 9))
    data = cleaned_bat.groupby(['fullName'])['runs'].sum().sort_values(ascending=False)[:10]
    x = data
    y = data.index
    plt.title("Total IPL Runs Scored By Individual Players 2008-21")
    plt.bar(y, x, color='#00F3D0')
    plt.xlabel('Batsman Names')
    plt.ylabel('Runs Scored')
    for bars in ax.containers:
    ax.bar_label(bars)
    plt.show()
![Visualization 5](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual5.png)

#### 7
    -
![Visualization 6](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual6.png)

#### 8
    -
![Visualization 7](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual7.png)

#### 9
    -
![Visualization 8](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual8.png)

#### 10
    -
![Visualization 9](https://github.com/Sumit21adm/Data-Visualization-Assesment/blob/28c12408ca6734e85559addb1071a06cb89f7bd6/Visualisation%20Outputs/visual9.png)

