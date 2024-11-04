import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from normalizer import unnormalize_thetas
from normalizer import get_mean
from normalizer import get_sigma

def hypothesis(X, thetas):
    return X@thetas

def cost_calculate(X, y, thetas):
	return np.sum((hypothesis(X, thetas) - y) **2) / (2 * len(y))

def gradient_descent(thetas, X, y):
	learning_rate = 0.1
	
	tmp_theta_1 = thetas[1] - (learning_rate * np.sum((hypothesis(X, thetas) - y) * X[:, 1]) / len(y))
	tmp_theta_0 = thetas[0] - (learning_rate * np.sum(hypothesis(X, thetas) - y) / len(y))

	return np.array([tmp_theta_0, tmp_theta_1])

if __name__ == '__main__':
	dataset = pd.read_csv('data.csv')
	km = dataset['km'].values
	price = dataset['price'].values

	km_mean = get_mean(km)
	km_sigma = get_sigma(km)
	km_normalized = (km - km_mean) / km_sigma

	m = len(km_normalized)
	X = np.c_[np.ones(m), km_normalized]
	y = price

	cost = 0
	new_cost = 0
	thetaA = 0
	thetaB = 0
	thetas = np.array([thetaB, thetaA])
	i = 0

	cost = cost_calculate(X, y, thetas)
	print('Initial thetaA:', thetas[1], 'thetaB:', thetas[0], 'cost:', cost)

	while True:
		thetas = gradient_descent(thetas, X, y)
		new_cost = cost_calculate(X, y, thetas)
		print('New calculated thetaA:', thetas[1], 'thetaB:', thetas[0], 'cost:', new_cost)
		if new_cost > cost:
			print("Gradient descent is complete, total iterations: ", i)
			break
		cost = new_cost
		i+=1

	print(unnormalize_thetas(km, thetas))

	# x = np.linspace(0, 10, 100)  # X-axis values
	# y = 2 * x + 3  # Y-axis values, representing a linear function y = 2x + 3

	# # Create a line plot
	# plt.plot(x, y, label='y = 2x + 3')

	# # Create a scatter plot (optional)
	# plt.scatter(x, y, color='red', label='Data points')

	# # Add titles and labels
	# plt.title('Graph of y = 2x + 3')
	# plt.xlabel('X-axis')
	# plt.ylabel('Y-axis')

	# # Display a legend (optional)
	# plt.legend()

	# # Show the plot
	# plt.show()
