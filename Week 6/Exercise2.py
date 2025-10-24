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

#c)
df = df.dropna()

#d)
df['quality'].hist()
plt.title('Distribution of Wine Quality Ratings')
plt.xlabel('Wine Quality')
plt.ylabel('Frequency')
plt.show()

plt.scatter(df['alcohol'], df['quality'])
plt.title('Quality vs Alcohol')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.show()