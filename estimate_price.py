# def print_graph(km, y, unnormalized_thetas):
# 	x_values = km
# 	y_values = y

# 	# Plotting the points
# 	plt.scatter(x_values, y_values, color='blue', marker='o')

# 	x_line = np.linspace(min(x_values), max(x_values), 100)
# 	a = unnormalized_thetas[1]
# 	b = unnormalized_thetas[0]
# 	y_line = a * x_line + b
# 	plt.plot(x_line, y_line, color='red', label=f'y = {a}x + {b}')

# 	# Labeling the axes
# 	plt.xlabel('Mileage')
# 	plt.ylabel('Price')

# 	# Adding a title
# 	text = f'Algorithm Precision: 1'
# 	plt.text(0.95, 0.05, text, horizontalalignment='right', verticalalignment='bottom', transform=plt.gca().transAxes)

# 	plt.title('Price of a car depending on its mileage')

# 	# Displaying the plot
# 	plt.show()

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
		estimate_price = a * user_input + b
		if estimate_price < 0:
			estimate_price = 0
		print(f"Estimated price: {estimate_price}")

	except ValueError:
		print("Please enter a valid mileage.")
	except FileNotFoundError:
		print(f"Error: The file was not found.")
	except IOError:
		print(f"Error: An I/O error occurred while accessing.")

if __name__ == "__main__":
    main()