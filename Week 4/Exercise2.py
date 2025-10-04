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

def calculate_total_sales(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """
    Calculate total sales and percentage contribution for a given column.

    Parameters:
        df (pd.DataFrame): The sales dataset.
        group_col (str): The column to group by (e.g., 'Category', 'Month', or 'Sales Manager').

    Returns:
        pd.DataFrame: A DataFrame with total sales and percentage contribution for each group.

    Author:
        Edwin
    """
    total_sales = df.groupby(group_col)['Sales'].sum().reset_index()
    total_sum = total_sales['Total Sales'].sum()
    total_sales.rename(columns={'Sales': 'Total Sales'}, inplace=True)
    total_sales['% of Total'] = (total_sales['Total Sales'] / total_sum * 100).round(2)
    return total_sales