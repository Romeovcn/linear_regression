import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_precision(x, y, a, b):
	predictions = []
	for i in range(len(x)):
		predictions.append(a * x[i] + b)
	
	precision = np.sum(abs(predictions - y)) / (len(y))
	return precision

def print_graph(theta0, theta1, user_input, estimated_price):
	"""
	Prints a graph with the dataset and the estimated price.

	Parameters: theta0 (float), theta1 (float), user_input (float), estimated_price (float)
	"""

	dataset = pd.read_csv('data.csv')
	km = dataset['km'].values
	y = dataset['price'].values

	x_values = km
	y_values = y

	plt.scatter(x_values, y_values, color='blue', marker='o')
	plt.scatter(user_input, estimated_price, color='green', marker='o')

	x_line = np.linspace(0, max(x_values), 100)
	a = theta1
	b = theta0
	y_line = a * x_line + b
	plt.plot(x_line, y_line, color='red', label=f'y = {a}x + {b}')

	plt.xlabel('Mileage')
	plt.ylabel('Price')

	precision = get_precision(km, y, a, b)
	text = f'Precision: +- {np.floor(precision)}'
	plt.text(0.95, 0.05, text, horizontalalignment='right', verticalalignment='bottom', transform=plt.gca().transAxes)

	plt.title('Price of a car depending on its mileage')

	manager = plt.get_current_fig_manager()
	manager.full_screen_toggle()
	plt.show()

def main():
	try:
		# --- Read Thetas --- #
		with open('thetas', 'r') as file:
			content = file.read()
		content = content.split()
		b = float(content[0])
		a = float(content[1])

		# --- Get user input --- #
		user_input = input("Please enter a mileage: ")
		user_input = float(user_input)
		if user_input < 0:
			print("Please enter a valid mileage.")
			return

		# --- Estimate price --- #
		estimated_price = a * user_input + b
		if estimated_price < 0:
			estimated_price = 0
		print(f"Estimated price: {estimated_price}")
		print_graph(b, a, user_input, estimated_price)

	except ValueError:
		print("Please enter a valid mileage.")
	except FileNotFoundError:
		print(f"Error: The file was not found.")
	except IOError:
		print(f"Error: An I/O error occurred while accessing.")

if __name__ == "__main__":
    main()