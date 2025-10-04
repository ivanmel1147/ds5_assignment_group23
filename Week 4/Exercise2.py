import pandas as pd
import numpy as np

# Load the dataset
# df = pd.read_excel('detailedRetail.xlsx')
# print(df.shape)
# df.head()

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load sales data from an Excel file.

    Parameters:
        file_path (str): Path to the Excel file.

    Returns:
        pd.DataFrame: The loaded sales dataset.

    Author:
        Edwin
    """
    return pd.read_excel(file_path)