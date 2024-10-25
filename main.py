import pandas as pd
import numpy as np
from normalizer import normalize_dataset
from normalizer import unnormalize_thetas
from normalizer import get_mean
from normalizer import get_sigma

def hypothesis(a, b, x):
    return x * a + b

def thetaA_calculate(a, b, dataset_array):
	total_cost = 0



def thetaB_calculate(a, b, dataset_array):
	total_cost = 0

	for element in dataset_array:
		x = element['km']
		y = element['price']
		prediction = hypothesis(a, b, x)
		cost = prediction - y
		total_cost += cost
 
	return total_cost / len(dataset_array)

def cost_calculate(X, y, thetas):
	return np.sum((X@thetas - y) **2) / (2 * len(y))

def gradient_descent(thetas, X):
	learning_rate = 0.1

	# for element in dataset_array:
	# 	x = element['km']
	# 	y = element['price']
	# 	prediction = hypothesis(a, b, x)
	# 	cost = prediction - y
	# 	cost = cost * x
	# 	total_cost += cost

	# return total_cost / len(dataset_array)

	# new_theta_A = thetaA - learning_rate * np.sum((X@thetas - y) **2) / (2 * len(y))
	# new_theta_B = thetaB - learning_rate * thetaB_calculate(thetas, X)

	x_mean = np.mean(X)
	y_mean = np.mean(y)
	print("X MEAN: ", x_mean)
	print("Y MEAN: ", y_mean)

	print(y - y_mean)
	# Step 2: Calculate theta1 (slope) using the formula
	# numerator = np.sum((X - x_mean) * (y - y_mean))
	# denominator = np.sum((X - x_mean) ** 2)
	# theta1 = numerator / denominator

	# Step 3: Calculate theta0 (intercept)
	# theta0 = y_mean - theta1 * x_mean

	return (1, 1)

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
	# y = y.reshape(24, 1)

	cost = 0
	new_cost = 0
	thetaA = -0.01
	thetaB = 4000
	thetas = np.array([thetaB, thetaA])
	# for e in X:
		# print(e[1], " y: ", hypothesis(thetaA, thetaB, e[1]))
	# print(X@thetas)
	# print(hypothesis(thetaA, thetaB, X) - y)

	print('=====================thetaA:', thetaA, 'thetaB:', thetaB, '=====================')
	cost = cost_calculate(X, y, thetas)
	# print("TOTAL COST: ", cost)	

	# while True:
	thetaA, thetaB = gradient_descent(thetas, X)
	# thetas = np.array([thetaB, thetaA])
	# print('=====================thetaA:', thetaA, 'thetaB:', thetaB, '=====================')
	# new_cost = cost_calculate(X, y, thetas)
	# if new_cost > cost:
		# print("TOTAL END COST: ", new_cost)
		# break
	# cost = new_cost
	# print("TOTAL COST: ", cost)
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

# for km datset: 2.6943321694490683 price: [3650] km prediction: 3999.9730566783055 cost: [122481.14040076]
# for km datset: 0.7511608134697138 price: [3800] km prediction: 3999.992488391865 cost: [39996.99541317]
# for km datset: 0.9586651399066309 price: [4400] km prediction: 3999.990413348601 cost: [160007.66941302]
# for km datset: 1.6379993973912297 price: [4450] km prediction: 3999.9836200060263 cost: [202514.74226288]
# for km datset: 1.4531847963684428 price: [5250] km prediction: 3999.9854681520364 cost: [1562536.32983108]
# for km datset: 0.26633762086009444 price: [5350] km prediction: 3999.9973366237914 cost: [1822507.19112286]
# for km datset: 1.2747698614881027 price: [5800] km prediction: 3999.987252301385 cost: [3240045.89187752]
# for km datset: -0.2339999139130328 price: [5990] km prediction: 4000.002339999139 cost: [3960090.6868089]
# for km datset: 0.8423075736803223 price: [5999] km prediction: 3999.991576924263 cost: [3996034.67552774]
# for km datset: -0.3309645524349567 price: [6200] km prediction: 4000.0033096455245 cost: [4839985.43757065]
# for km datset: -0.36918801294029907 price: [6390] km prediction: 4000.0036918801293 cost: [5712082.35282661]
# for km datset: -0.7370524585647739 price: [6390] km prediction: 4000.0073705245854 cost: [5712064.76894681]
# for km datset: -0.5248938294788045 price: [6600] km prediction: 4000.0052489382947 cost: [6759972.70554842]
# for km datset: -0.0691600284257622 price: [6800] km prediction: 4000.0006916002844 cost: [7839996.12703889]
# for km datset: -0.6606443234094979 price: [6800] km prediction: 4000.006606443234 cost: [7839963.00396154]
# for km datset: -0.48562315087742525 price: [6900] km prediction: 4000.0048562315087 cost: [8409971.83388083]
# for km datset: -1.024552611782278 price: [6900] km prediction: 4000.0102455261176 cost: [8409940.57605349]
# for km datset: -0.15642820309549368 price: [6990] km prediction: 4000.001564282031 cost: [8940090.6455959]
# for km datset: -0.7779909289487301 price: [7490] km prediction: 4000.0077799092896 cost: [12180045.69629369]
# for km datset: -0.686359345545512 price: [7555] km prediction: 4000.0068635934554 cost: [12637976.19989764]
# for km datset: -0.9127523835664999 price: [7990] km prediction: 4000.0091275238356 cost: [15920027.1624431]
# for km datset: -0.6315549318529207 price: [7990] km prediction: 4000.0063155493185 cost: [15920049.60195632]
# for km datset: -1.5158918281005709 price: [7990] km prediction: 4000.015158918281 cost: [15919979.03206191]
# for km datset: -0.761700869677047 price: [8290] km prediction: 4000.007617008697 cost: [18404034.6461234]
# TOTAL COST:  [3553174.89818452]
