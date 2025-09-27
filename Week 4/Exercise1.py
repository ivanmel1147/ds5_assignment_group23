import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('hotelBookings.xlsx')
print(df.shape)
df.head()

# Mistakes in the dataset
# 1. Duplicate rows
# 2. Missing values

