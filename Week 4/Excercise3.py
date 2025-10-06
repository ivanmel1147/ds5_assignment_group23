import pandas as pd
import numpy as np
from langdetect import detect, DetectorFactory, LangDetectException

# 3.1
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

def fix_encoding_issues(text: str) -> str:
    """
    Fixes misencoded text such as 'Ã¼' -> 'ü'.

    Args:
        text (str): Text potentially containing encoding artifacts.

    Returns:
        str: Cleaned text with corrected encoding.

    Author:
        Edwin
    """
    if not isinstance(text, str):
        return ""
    try:

        return text.encode("latin1").decode("utf-8")
    except Exception:
        return text

