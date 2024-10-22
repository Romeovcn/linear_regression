import pandas as pd
import pandas as np
from normalizer import normalize_dataset
from normalizer import unnormalize_thetas
# from normalizer import normalize_value
# from normalizer import unnormalize_value

def hypothesis(a, b, x):
    return b + a * x

def thetaA_calculate(a, b, dataset_array):
	total_cost = 0

	for element in dataset_array:
		x = element['km']
		y = element['price']
		prediction = hypothesis(a, b, x)
		cost = prediction - y
		cost = cost * x
		total_cost += cost

	return total_cost / len(dataset_array)

def thetaB_calculate(a, b, dataset_array):
	total_cost = 0

	for element in dataset_array:
		x = element['km']
		y = element['price']
		prediction = hypothesis(a, b, x)
		cost = prediction - y
		total_cost += cost
 
	return total_cost / len(dataset_array)

def cost_calculate(a, b, dataset_array):
	total_cost = 0

	for element in dataset_array:
		prediction = hypothesis(a, b, element['km'])
		cost = prediction - element['price']
		cost = cost**2
		total_cost += cost
		print('for km datset:', element['km'], 'price:', element['price'], 'km prediction:', prediction,'cost:', cost)
 
	return total_cost / (2 * len(dataset_array))

def gradient_descent(thetaA, thetaB, dataset_array):
	learning_rate = 0.1

	new_theta_A = thetaA - learning_rate * thetaA_calculate(thetaA, thetaB, dataset_array)
	new_theta_B = thetaB - learning_rate * thetaB_calculate(thetaA, thetaB, dataset_array)

	return (new_theta_A, new_theta_B)

if __name__ == '__main__':
	dataset = pd.read_csv('data.csv')
	dataset_array = dataset.to_dict(orient='records')
	normalized_dataset_array = normalize_dataset(dataset_array)

	cost = 0
	new_cost = 0
	thetaB = 0
	thetaA = 0
	
	print('=====================thetaA:', thetaA, 'thetaB:', thetaB, '=====================')
	cost = cost_calculate(thetaA, thetaB, normalized_dataset_array)
	print("TOTAL COST: ", cost)

	while True:
		thetaA, thetaB = gradient_descent(thetaA, thetaB, normalized_dataset_array)
		print('=====================thetaA:', thetaA, 'thetaB:', thetaB, '=====================')
		new_cost = cost_calculate(thetaA, thetaB, normalized_dataset_array)
		if new_cost > cost:
			print("TOTAL END COST: ", new_cost)
			break
		cost = new_cost
		print("TOTAL COST: ", cost)
	print('==========================================')

	print(unnormalize_thetas(thetaA, thetaB, dataset_array))