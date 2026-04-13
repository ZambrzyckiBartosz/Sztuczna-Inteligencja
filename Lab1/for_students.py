import numpy as np
import matplotlib.pyplot as plt

from data import get_data, inspect_data, split_data

data = get_data()
inspect_data(data)

train_data, test_data = split_data(data)

y_train = train_data['MPG'].to_numpy()
x_train = train_data['Weight'].to_numpy()

y_test = test_data['MPG'].to_numpy()
x_test = test_data['Weight'].to_numpy()

# TODO: calculate closed-form solution

m = x_train.size
x_matrix = np.concatenate((np.ones((m, 1)), x_train.reshape(-1, 1)), 1)
y_matrix = y_train.reshape(-1, 1)
theta_matrix = np.linalg.inv(x_matrix.T.dot(x_matrix)).dot(x_matrix.T).dot(y_matrix)
theta_best = theta_matrix.flatten()

# TODO: calculate error

mse = np.mean(((theta_best[1] * x_test + theta_best[0]) - y_test) ** 2)
print("MSE:", mse)

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
x_std  = np.std(x_train)
y_mean = np.mean(y_train)
y_std  = np.std(y_train)

x_train = (x_train - x_mean) / x_std
y_train = (y_train - y_mean) / y_std

x_matrix = np.concatenate((np.ones((m, 1)), x_train.reshape(-1,1)), 1)
y_matrix = y_train.reshape(-1, 1)

# TODO: calculate theta using Batch Gradient Descent

theta_best = np.random.rand(1, 2).reshape(-1, 1)
learning_rate = 0.001
max_epoch = 100000

for i in range(max_epoch):
    gradientMse = (2/m) * x_matrix.T.dot(x_matrix.dot(theta_best) - y_matrix)
    theta_best = theta_best - learning_rate * gradientMse

theta_best = theta_best.flatten()

# TODO: calculate error

x_standarized = (x_test - x_mean) / x_std
y_result = theta_best[1] * x_standarized + theta_best[0]
y_prediction = (y_result * y_std) + y_mean

mse = np.mean((y_prediction - y_test) ** 2)

print("MSE2:", mse)


x = np.linspace(min(x_test), max(x_test), 100)
x_standarized = (x - x_mean) / x_std
y_standarized = float(theta_best[0]) + float(theta_best[1]) * x_standarized
y = (y_standarized * y_std) + y_mean
plt.plot(x, y)
plt.scatter(x_test, y_test)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()
