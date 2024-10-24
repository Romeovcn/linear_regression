import pandas as pd
import numpy as np
from normalizer import normalize_dataset
from normalizer import unnormalize_thetas
from normalizer import get_mean
from normalizer import get_sigma

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

def cost_calculate(a, b, X, y):
	total_cost = 0
	i = 0
	print(X)
	print("====================================")
	# print(hypothesis(a, b, X) - y)
	print(y)

	# for element in X:
	# 	prediction = hypothesis(a, b, element[1])
	# 	cost = prediction - y[i]
	# 	cost = cost**2
	# 	total_cost += cost
	# 	# print('for km datset:', element['km'], 'price:', element['price'], 'km prediction:', prediction,'cost:', cost)
	# 	i += 1

	return total_cost / (2 * len(y))

def gradient_descent(thetaA, thetaB, dataset_array):
	learning_rate = 0.1

	new_theta_A = thetaA - learning_rate * thetaA_calculate(thetaA, thetaB, dataset_array)
	new_theta_B = thetaB - learning_rate * thetaB_calculate(thetaA, thetaB, dataset_array)

	return (new_theta_A, new_theta_B)

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

	print(y[3])

	cost = 0
	new_cost = 0
	thetaB = 0
	thetaA = 0

	print('=====================thetaA:', thetaA, 'thetaB:', thetaB, '=====================')
	cost = cost_calculate(thetaA, thetaB, X, y)
	print("TOTAL COST: ", cost)	

	# while True:
	# 	thetaA, thetaB = gradient_descent(thetaA, thetaB, normalized_dataset_array)
	# 	print('=====================thetaA:', thetaA, 'thetaB:', thetaB, '=====================')
	# 	new_cost = cost_calculate(thetaA, thetaB, normalized_dataset_array)
	# 	if new_cost > cost:
	# 		print("TOTAL END COST: ", new_cost)
	# 		break
	# 	cost = new_cost
	# 	print("TOTAL COST: ", cost)
	# print('==========================================')

	# print(unnormalize_thetas(thetaA, thetaB, dataset_array))

# for km datset: 2.6943321694490683 price: 3650 km prediction: 0.0 cost: 13322500.0
# for km datset: 0.7511608134697138 price: 3800 km prediction: 0.0 cost: 14440000.0
# for km datset: 0.9586651399066309 price: 4400 km prediction: 0.0 cost: 19360000.0
# for km datset: 1.6379993973912297 price: 4450 km prediction: 0.0 cost: 19802500.0
# for km datset: 1.4531847963684428 price: 5250 km prediction: 0.0 cost: 27562500.0
# for km datset: 0.26633762086009444 price: 5350 km prediction: 0.0 cost: 28622500.0
# for km datset: 1.2747698614881027 price: 5800 km prediction: 0.0 cost: 33640000.0
# for km datset: -0.2339999139130328 price: 5990 km prediction: 0.0 cost: 35880100.0
# for km datset: 0.8423075736803223 price: 5999 km prediction: 0.0 cost: 35988001.0
# for km datset: -0.3309645524349567 price: 6200 km prediction: 0.0 cost: 38440000.0
# for km datset: -0.36918801294029907 price: 6390 km prediction: 0.0 cost: 40832100.0
# for km datset: -0.7370524585647739 price: 6390 km prediction: 0.0 cost: 40832100.0
# for km datset: -0.5248938294788045 price: 6600 km prediction: 0.0 cost: 43560000.0
# for km datset: -0.0691600284257622 price: 6800 km prediction: 0.0 cost: 46240000.0
# for km datset: -0.6606443234094979 price: 6800 km prediction: 0.0 cost: 46240000.0
# for km datset: -0.48562315087742525 price: 6900 km prediction: 0.0 cost: 47610000.0
# for km datset: -1.024552611782278 price: 6900 km prediction: 0.0 cost: 47610000.0
# for km datset: -0.15642820309549368 price: 6990 km prediction: 0.0 cost: 48860100.0
# for km datset: -0.7779909289487301 price: 7490 km prediction: 0.0 cost: 56100100.0
# for km datset: -0.686359345545512 price: 7555 km prediction: 0.0 cost: 57078025.0
# for km datset: -0.9127523835664999 price: 7990 km prediction: 0.0 cost: 63840100.0
# for km datset: -0.6315549318529207 price: 7990 km prediction: 0.0 cost: 63840100.0
# for km datset: -1.5158918281005709 price: 7990 km prediction: 0.0 cost: 63840100.0
# for km datset: -0.761700869677047 price: 8290 km prediction: 0.0 cost: 68724100.0
# TOTAL COST:  20880519.291666668
