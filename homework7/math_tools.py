def addition(a, b):		# Adds the inputs a and b
	sum = a + b
	return sum

def subtraction(a, b):		# Subtracts the inputs a and b
	diff = a - b
	return diff


def multiplication(a, b):	# Multiplies a and b
	product = a*b
	return product


def division(a, b):		# Divides a by b, and compensates for any division by zero
	if b == 0:
		print("Divide by zero error.")
	else:
		ratio = a/b
		return ratio
