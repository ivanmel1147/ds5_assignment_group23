import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#a)
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

#b)
print(df.shape)
print(df.describe())
print(df.info())