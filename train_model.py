import pandas as pd
import numpy as np

GREEN = "\033[92m"  # Green
YELLOW = "\033[93m"  # Yellow
RESET = "\033[0m"  # Reset to default color

def unnormalize_thetas(X, thetas):
	feat_mean = get_mean(X)
	feat_sigma = get_sigma(X)

	thetas[1] = thetas[1] / feat_sigma
	thetas[0] = thetas[0] - (thetas[1] * feat_mean)
	return thetas

def get_mean(array):
	mean = 0
	for element in array:
		mean += element
	mean = mean / len(array)
	return mean

def get_sigma(array):
	sigma = 0
	mean = get_mean(array)
	for element in array:
		sigma += (element - mean)**2
	sigma = sigma / len(array)
	sigma = sigma**0.5
	return sigma

def hypothesis(X, thetas):
	"""
	Method to calculate the hypothesis from a matrix X and thetas by performing a matrix multiplication.

	Parameters: X (Matrix filled with the mileage and 1's), thetas (Matrix filled with thetas)
	Returns: A matrix with the hypothesis
	"""
	return X@thetas

def cost_calculate(X, y, thetas):
	return np.sum((hypothesis(X, thetas) - y) **2) / (2 * len(y))

def gradient(thetas, X, y):
	learning_rate = 0.1
	
	tmp_theta_1 = thetas[1] - (learning_rate * np.sum((hypothesis(X, thetas) - y) * X[:, 1]) / len(y))
	tmp_theta_0 = thetas[0] - (learning_rate * np.sum(hypothesis(X, thetas) - y) / len(y))

	return np.array([tmp_theta_0, tmp_theta_1])

def gradient_descent(X, y):
	thetas = np.array([0, 0])
	new_cost = 0
	max_iterations = 1000
	cost = cost_calculate(X, y, thetas)

	print(f'{YELLOW}Initial thetaA: {thetas[1]}, thetaB: {thetas[0]}, cost: {cost}{RESET}')

	for i in range(max_iterations):
		thetas = gradient(thetas, X, y)
		new_cost = cost_calculate(X, y, thetas)
		print(f'{YELLOW}New calculated thetaA: {thetas[1]}, thetaB: {thetas[0]}, cost: {new_cost}, iterations: {i}{RESET}')
		if new_cost > cost or abs(new_cost - cost) < 1e-6:
			break
		cost = new_cost
	
	return thetas

def main():
	# --- Read data --- #
	np.set_printoptions(suppress=True)
	dataset = pd.read_csv('data.csv')
	km = dataset['km'].values

	# --- Normalize dataset --- #
	km_mean = get_mean(km)
	km_sigma = get_sigma(km)
	km_normalized = (km - km_mean) / km_sigma

	# --- Set variables --- #
	m = len(km_normalized)
	X = np.c_[np.ones(m), km_normalized]
	y = dataset['price'].values

	# --- Apply gradient descent --- #
	thetas = gradient_descent(X, y)

	# --- Get result --- #
	unnormalized_thetas = unnormalize_thetas(km, thetas)
	print(f"{GREEN}Gradient descent is complete, theta_0: {unnormalized_thetas[0]}, theta_1: {unnormalized_thetas[1]}{RESET}")
	result_string = f"{str(unnormalized_thetas[0])} {str(unnormalized_thetas[1])}"
	with open('thetas', 'w') as file:
		file.write(result_string)

if __name__ == '__main__':
	main()