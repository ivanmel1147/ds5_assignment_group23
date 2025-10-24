#a)
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)  

x = np.random.uniform(0, 10, 200)
y = 2 * x**2 - 5 * x + 3 + np.random.normal(0, 10, 200)

# Plot the dataset
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y') 
plt.title('Dataset') 
plt.show()   

#b)
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

#c)
plt.scatter(train_x, train_y)
plt.xlabel('x')
plt.ylabel('y') 
plt.title('Dataset') 
plt.show() 

plt.scatter(test_x, test_y)
plt.xlabel('x')
plt.ylabel('y') 
plt.title('Dataset') 
plt.show()

# Type of relationship: Non-linear, quadratic
# Regression model: Polynomial Regression (degree 2) - y = ax^2 + bx + 

#d)
import numpy as np
import statsmodels.api as sm
from sklearn.metrics import r2_score, mean_squared_error

#Train the polynomial regression model (degree 2) using statsmodels
X_train = np.column_stack((train_x, train_x**2))
X_train = sm.add_constant(X_train)  # add intercept term
model = sm.OLS(train_y, X_train).fit()

#e)
#Evaluate the model on test data
X_test = np.column_stack((test_x, test_x**2))
X_test = sm.add_constant(X_test)
y_pred = model.predict(X_test)

print(model.summary())  # Optional: detailed regression results
print(f"R²: {r2_score(test_y, y_pred):.4f}")
print(f"MSE: {mean_squared_error(test_y, y_pred):.4f}")


