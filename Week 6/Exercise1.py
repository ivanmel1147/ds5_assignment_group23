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
