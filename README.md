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

### Import Packages
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from collections import Counter

### Loading/ Importing Dataset
    batdataset = pd.read_csv('datasets/all_season_batting_card.csv')
    balldataset = pd.read_csv('datasets/all_season_bowling_card.csv')
    all_matches = pd.read_csv('datasets/all_season_summary.csv')

### View Batting Dataset (First 10)
    print(batdataset.head(10))

### View Balling Dataset (First 10)
    print(balldataset.head(10))

### Selecting Required Columns To Create New Cleaned Dataset
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
    null1 = cleaned_bat.isna().sum()
    print(null1)
### 

### 

### 


### List Of Visualizations
#### 1
    -
#### 2
    -
#### 3
    - 
#### 4
    -
#### 5
    -
#### 6
    -
#### 7
    -
#### 8
    -
#### 9
    -
#### 10
    -
