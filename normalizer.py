import copy

def normalize_dataset(dataset_array):
	normalized_array = copy.deepcopy(dataset_array)
	array = [obj['km'] for obj in dataset_array]
	mean = get_mean(array)
	sigma = get_sigma(array)
	for element in normalized_array:
		# print(element)
		element['km'] = (element['km'] - mean) / sigma
	return normalized_array

def unnormalize_thetas(thetaA, thetaB, dataset_array):
	array = [obj['km'] for obj in dataset_array]
	target_array = [obj['price'] for obj in dataset_array]

	feat_mean = get_mean(array)
	feat_sigma = get_sigma(array)

	thetaA = thetaA / feat_sigma
	thetaB = thetaB - (thetaA * feat_mean)
	return (thetaA, thetaB)

# def normalize_value(value, dataset_array):
# 	mean = get_mean(dataset_array)
# 	sigma = get_sigma(dataset_array)
# 	return (value - mean) / sigma

# def unnormalize_value(value, dataset_array):
# 	array = [obj['km'] for obj in dataset_array]
# 	mean = get_mean(dataset_array)
# 	sigma = get_sigma(dataset_array)
# 	return value * sigma + mean

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