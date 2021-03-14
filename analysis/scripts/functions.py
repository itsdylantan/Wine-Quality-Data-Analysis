
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):
​
    # Method Chain 1 (Load data, deal with missing data, and make data readable)
​
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .dropna()
          .sort_values("alcohol", ascending=False)
          .sort_values("fixed acidity", ascending=False)
          .reset_index(drop=True)
      )
​
    # Method Chain 2 (Create new columns, drop others, and do processing)
​
     df2 = (
          df1
          .rename(columns={"free sulfur dioxide": "free SO2"})
          .rename(columns={"total sulfur dioxide": "total SO2"})
          .assign(High_quality = lambda x: x['quality']>4)
          .loc[df1['residual sugar']>15]
      )
​
    # Make sure to return the latest dataframe
​
    return df2