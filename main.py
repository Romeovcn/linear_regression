import pandas as pd
import pandas as np

def hypothesis(theta_a, theta_b, x):
    return theta_b + theta_a * x

def thetaA_calculate(a, b, dataset_array):
	total_cost = 0

	for element in dataset_array:
		prediction = hypothesis(a, b, element['km'])
		cost = prediction - element['price']
		cost = cost * element['km']
		total_cost += cost

	return total_cost / len(dataset_array)

def thetaB_calculate(a, b, dataset_array):
	total_cost = 0

	for element in dataset_array:
		prediction = hypothesis(a, b, element['km'])
		cost = prediction - element['price']
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
	learning_rate = 0.001

	# new_theta_A = thetaA - learning_rate * thetaA_calculate(thetaA, thetaB, dataset_array)
	# new_theta_B = thetaB - learning_rate * thetaB_calculate(thetaA, thetaB, dataset_array)

	h = hypothesis(thetaA, thetaB, x)
	new_theta_B -= thetaA * (1 / len(dataset_array)) * np.sum(h - y)
	new_theta_A -= thetaA * (1 / len(dataset_array)) * np.sum((h - y) * x)	
	
	return (new_theta_A, new_theta_B)

if __name__ == '__main__':
	dataset = pd.read_csv('data.csv')
	dataset_array = dataset.to_dict(orient='records')
	cost = 0
	new_cost = 0
	thetaB = 0
	thetaA = 0

	print('=====================thetaA:', thetaA, 'thetaB:', thetaB, '=====================')
	cost = cost_calculate(thetaA, thetaB, dataset_array)
	print("TOTAL COST: ", cost)

	while True:
		thetaA, thetaB = gradient_descent(thetaB, thetaA, dataset_array)
		print('=====================thetaA:', thetaA, 'thetaB:', thetaB, '=====================')
		new_cost = cost_calculate(thetaA, thetaB, dataset_array)
		if new_cost > cost:
			print("TOTAL END COST: ", new_cost)
			break
		cost = new_cost
		print("TOTAL COST: ", cost)

	# for element in data_array:
	# 	print(element)