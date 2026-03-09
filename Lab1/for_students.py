import numpy as np
import matplotlib.pyplot as plt

from ans import x_standarized, learning_rate, y_pred
from data import get_data, inspect_data, split_data

data = get_data()
inspect_data(data)

train_data, test_data = split_data(data)

# Simple Linear Regression
# predict MPG (y, dependent variable) using Weight (x, independent variable) using closed-form solution
# y = theta_0 + theta_1 * x - we want to find theta_0 and theta_1 parameters that minimize the prediction error

# We can calculate the error using MSE metric:
# MSE = SUM (from i=1 to n) (actual_output - predicted_output) ** 2

# get the columns
y_train = train_data['MPG'].to_numpy()
x_train = train_data['Weight'].to_numpy()

y_test = test_data['MPG'].to_numpy()
x_test = test_data['Weight'].to_numpy()

# TODO: calculate closed-form solution
theta_best = [0,0]

m = x_train.size
x_matrix = np.concatenate((np.ones((m,1)),x_train.reshape(-1,1)),1)
y_matrix = y_train.reshape(-1,1)
theta_matrix = np.linalg.inv(x_matrix.T.dot(x_matrix)).dot(x_matrix.T).dot(y_matrix)
thehta_best = theta_matrix.flatten()
# TODO: calculate error

mse = np.mean(((theta_best[1] * x_test + theta_best[0]) - y_test) ** 2)

# plot the regression line


x = np.linspace(min(x_test), max(x_test), 100)
y = float(theta_best[0]) + float(theta_best[1]) * x
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()

print()
# TODO: standardization
x_mean = np.mean(x_train)
y_mean = np.mean(y_train)
x_std = np.std(x_train)
y_std = np.std(y_train)

x_train = (x_train - x_mean) / x_std
y_train = (y_train - y_mean) / y_std
x_matrix = np.concatenate((np.ones((m,1)),x_train.reshape(-1,1)),1)
y_matrix = y_train.reshape(-1,1)

theta_best = np.random.rand(1,2).reshape(-1,1)
learning_rate = 0.001
max_iter = 1000
for i in range(max_iter):
    gradient = (2/m) * x_matrix.T.dot(x_matrix.dot(theta_best) - y_matrix)
    theta_best = theta_best - learning_rate * gradient

theta_best = theta_best.flatten()


# TODO: calculate theta using Batch Gradient Descent

# TODO: calculate error

x_standarized = (x_test - x_mean) / x_std
y_standarized = (y_test - y_mean) / y_std
y_pred = (y_standarized * y_std) * y_mean

mse = np.mean((y_pred - y_std) ** 2)
# plot the regression line
x = np.linspace(min(x_test), max(x_test), 100)
y = float(theta_best[0]) + float(theta_best[1]) * x
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()