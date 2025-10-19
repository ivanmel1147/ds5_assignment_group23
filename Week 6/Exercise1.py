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
# Regression model: Polynomial Regression (degree 2) - y = ax^2 + bx + c