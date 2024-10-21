import pandas as pd

def cost_calculate(a, b, dataset_array):
	total_cost = 0

	for element in dataset_array:
		found = a * element['km'] + b
		cost = found - element['price']
		cost = cost**2
		total_cost += cost

		# print('for km datset:', element['km'], 'price:', element['price'], 'km found:', found,'cost:', cost)
	
	# print('total cost: ', total_cost / (2 * len(dataset_array)))
	return total_cost / (2 * len(dataset_array))



if __name__ == '__main__':
	dataset = pd.read_csv('data.csv')
	dataset_array = dataset.to_dict(orient='records')

	# print(dataset_array)
	cost_calculate(0, 0, dataset_array)

	# for element in data_array:
	# 	print(element)