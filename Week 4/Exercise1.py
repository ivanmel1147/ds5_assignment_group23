import pandas as pd
import numpy as np

# Load the dataset
#df = pd.read_excel('hotelBookings.xlsx')
#print(df.shape)
#df.head()

# Mistakes in the dataset
# 1. Duplicate rows
# 2. Missing values

# 1. Handling duplicate rows
# data1_clean = df.drop_duplicates()
# data1_clean

# 2. Handling missing values
# data2_clean = data1_clean.dropna()
# data2_clean

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load a dataset from an Excel file.

    Parameters:
        file_path (str): The path to the Excel file to load.

    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame.

    Author:
        Edwin
    """
    return pd.read_excel(file_path)

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: A new DataFrame with duplicate rows removed.
    
    Author:
        Edwin
    """
    return df.drop_duplicates()