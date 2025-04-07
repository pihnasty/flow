import csv
import os
import os.path as path

import numpy as np
import pandas as pd


def make_dir_if_not(fileName):
    if not path.isdir(fileName):
        os.makedirs(fileName)


def save_to_csv(main_df, joined_df, path, file_name):
    df = main_df.join(joined_df)
    print(df)
    make_dir_if_not(path)
    df.to_csv(path + file_name, sep=';', index=True, quotechar='"', quoting=csv.QUOTE_ALL)

def replace_dish_to_mean(df):
    """
    Replacing missing values with column averages
    :param df: initial df
    :return: Replaced df
    """
    df = df.applymap(lambda x: np.nan if isinstance(x, str) and x.strip() == '-' else x)
    # Convert columns with numeric values to a numeric data type
    df = df.apply(pd.to_numeric, errors='ignore')
    # Replacing missing values with column averages
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            mean_value = df[col].mean()
            df[col].fillna(mean_value, inplace=True)
    return df
