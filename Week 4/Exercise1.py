import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('hotelBookings.xlsx')
print(df.shape)
df.head()

# Mistakes in the dataset
# 1. Duplicate rows
# 2. Missing values

# 1. Handling duplicate rows
data1_clean = df.drop_duplicates()
data1_clean

# 2. Handling missing values
data2_clean = data1_clean.dropna()
data2_clean