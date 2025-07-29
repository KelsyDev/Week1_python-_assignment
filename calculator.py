# 🧮 Simple Calculator that shows all 4 operations

# Ask for the first number
number1 = input("Type the first number: ")

# Ask for the second number
number2 = input("Type the second number: ")

# Change both inputs into numbers
number1 = float(number1)
number2 = float(number2)

# Do all the math
add = number1 + number2
subtract = number1 - number2
multiply = number1 * number2
divide = number1 / number2  # be careful! this only works if number2 isn't 0

# Show all results
print("Here are the results:")
print("Addition: ", number1, "+", number2, "=", add)
print("Subtraction: ", number1, "-", number2, "=", subtract)
print("Multiplication: ", number1, "*", number2, "=", multiply)
print("Division: ", number1, "/", number2, "=", divide)
