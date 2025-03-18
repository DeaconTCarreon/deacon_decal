import math_tools as tls

print("Welcome to the Calculator!")

history = []

while True:

	user_input = input("Enter something to begin, or type 'exit' to quit: ")

	if user_input.lower() == 'exit':
		print("Thank you, have a great day. Goodbye!")
		break
	
	a = float(input("Enter a: "))
	b = float(input("Enter b: "))

	operation = input("Enter your desired operation: addition, subtraction, multiplication, division: ")

	if operation == "addition":
		add = tls.addition(a, b)
		print(add)
		history.append(add)

	if operation == "subtraction":
		sub = tls.subtraction(a, b)
		print(sub)
		history.append(sub)

	if operation == "multiplication":
		mult = tls.multiplication(a, b)
		print(mult)
		history.append(mult)

	if operation == "division": 
		divide = tls.division(a, b)
		print(divide)
		history.append(divide)
	
	viewhistory = input("Would you like to see the history? ('Yes' or 'No')")
	if viewhistory == 'Yes':
		print(history)
