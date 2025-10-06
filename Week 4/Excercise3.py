import pandas as pd
import numpy as np
import re
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

def clean_tweet(text: str) -> str:
    """
    Cleans a tweet by fixing encoding, removing URLs, mentions, hashtags, emojis, and excess whitespace.

    Args:
        text (str): The raw tweet text.

    Returns:
        str: Cleaned tweet text.
    
    Author:
        Edwin
    """
    if not isinstance(text, str):
        return ""

    text = fix_encoding_issues(text)

    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    text = re.sub(r"[@#]\w+", "", text)

    text = re.sub(r"[^\w\sÀ-ÿ]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


#ex3.2(1&2)

from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

def analyze_sentiment_english(tweet: str) -> str:
    """
    Analyze sentiment of an English tweet using TextBlob.

    Parameters:
    tweet (str): The tweet text in English.

    Returns:
    str: 'positive' if polarity > 0,
         'negative' if polarity < 0,
         'neutral' otherwise.

    Author: Bronswhite
    """
    blob = TextBlob(tweet)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'


def analyze_sentiment_other(tweet: str) -> str:
    """
    Analyze sentiment of a non-English tweet using NLTK's SentimentIntensityAnalyzer.

    Parameters:
    tweet (str): The tweet text in any language other than English.

    Returns:
    str: 'positive' if compound score >= 0.05,
         'negative' if compound score <= -0.05,
         'neutral' otherwise.

    Author: Bronswhite
    """
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(tweet)
    compound = scores['compound']
    if compound >= 0.05:
        return 'positive'
    elif compound <= -0.05:
        return 'negative'
    else:
        return 'neutral'
