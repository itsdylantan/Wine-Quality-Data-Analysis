import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):

# Method Chain 1 (Load data, deal with missing data, and make data readable)
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .dropna()
        .sort_values("alcohol", ascending=False)
        .sort_values("fixed acidity", ascending=False)
        .reset_index(drop=True)
        )

# Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (df1
        .rename(columns = {"total sulfur dioxide":"total SO2"})
        .drop(columns = ['free sulfur dioxide'])                  #we can just use total to avoid redundancy
        .assign(high_quality = lambda x: x['quality']>4) #removes outliers from quality
        .loc[df1['residual sugar']<20] #removes outliers from variables using limits determined by box plots
        .loc[df1['residual sugar']>2]
          .loc[df1['fixed acidity']<9]
        .loc[df1['volatile acidity']<0.52]
        .loc[df1['citric acid']<0.55]
      )
# Make sure to return the latest dataframe
    return df2

def refine_data(dataframe): #Refine the dataset down by removing outiers and 
    dataframe = (dataframe[dataframe['high_quality']==True]
                 .drop(columns = ['high_quality'])
                 .reset_index(drop = True) # resets the index for the data set after removing rows during data cleaning
                 )
 
    return dataframe