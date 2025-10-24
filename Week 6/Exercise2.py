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

#e)
# Task by: Bronswhite 
# We first separate features and target, then split into training and test sets (80/20).
from sklearn.model_selection import train_test_split

X = df.drop('quality', axis=1)
y = df['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train set shape:", X_train.shape)
print("Test set shape:", X_test.shape)


#f)
# Task by: Bronswhite
# We'll experiment with two models: Linear Regression.
from sklearn.linear_model import LinearRegression

linreg_model = LinearRegression()



#g)
# Task by: Bronswhite
# Fit both models on the training data.
linreg_model.fit(X_train, y_train)
rfr_model.fit(X_train, y_train)


#h)
# Task by: Bronswhite
# Evaluate predictions using R^2 score for both models.
linreg_r2 = linreg_model.score(X_test, y_test)
rfr_r2 = rfr_model.score(X_test, y_test)

print("Linear Regression R^2 score:", linreg_r2)
print("Random Forest R^2 score:", rfr_r2)


