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

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in a DataFrame.

    
Numeric columns: fill missing values with the column mean.
Categorical columns: fill missing values with the mode (most frequent value).
Columns that are entirely missing are dropped.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns pd.DataFrame - a new DataFrame with missing values handled.

    Author:
        Ivan
    """
    df = df.copy()

    # Drop columns where all values are missing
    df.dropna(axis=1, how='all', inplace=True)

    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']:
            # Fill numeric NaNs with mean
            mean_value = df[column].mean()
            df[column].fillna(mean_value, inplace=True)
        else:
            # Fill categorical NaNs with mode (most frequent value)
            mode_value = df[column].mode()
            if not mode_value.empty:
                df[column].fillna(mode_value[0], inplace=True)
            else:
                df[column].fillna('Unknown', inplace=True)

    return df


def separate_categorical_numerical(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Separate the DataFrame into categorical and numerical DataFrames.

    Parameters:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: A tuple containing two DataFrames:
            - The first with only categorical columns.
            - The second with only numerical columns.

    Author:
        Bronswhite
    """
    categorical_df = df.select_dtypes(include=['object', 'category'])
    numerical_df = df.select_dtypes(include=['number'])
    return categorical_df, numerical_df 

def clean_hotel_bookings_data(file_path: str) -> pd.DataFrame:
    """
    Load and clean the hotel bookings dataset by performing all cleaning steps:
    - Load data
    - Remove duplicates
    - Handle missing values
    - (Optional) Separate categorical and numerical data for further processing

    Parameters:
        file_path (str): Path to the Excel file.

    Returns:
        pd.DataFrame: The fully cleaned DataFrame.

    Author:
        Bronswhite
    """
    df = load_data(file_path)
    df = remove_duplicates(df)
    df = handle_missing_values(df)
    # Optionally separate data if needed for further processing
    # categorical_df, numerical_df = separate_categorical_numerical(df)
    return df 