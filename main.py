import pandas as pd

def cost_calculate(a, b, dataset_array):
	total_cost = 0
	costs = []

	for element in dataset_array:
		found = a * element['km'] + b
		cost = found - element['price']
		cost = cost
		# total_cost += element['cost'] - (a * element['km'] + b)

		costs.append({
			"km": element['km'],
			"price": a * element['km'] + b
		})
		print('for km datset:', element['km'], 'price:', element['price'], 'cost:', cost)
	
	# print('total cost: ', total_cost / len(dataset_array))



if __name__ == '__main__':
	dataset = pd.read_csv('data.csv')
	dataset_array = dataset.to_dict(orient='records')

	cost_calculate(0.04, 1, dataset_array)

	# for element in data_array:
	# 	print(element)