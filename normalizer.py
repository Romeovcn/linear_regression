import copy

def unnormalize_thetas(X, thetas):
	feat_mean = get_mean(X)
	feat_sigma = get_sigma(X)

	thetaA = thetas[1] / feat_sigma
	thetaB = thetas[0] - (thetaA * feat_mean)
	return (thetaB, thetaA)

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