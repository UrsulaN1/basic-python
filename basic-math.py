
# maths.py

print("Welcome to the Python 2026 Math Program!")

# Ask the user for their name
name = input("Please enter your name: ")
print(f"Hello {name}, let's do some Math.")

# Get two numbers from the user
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division safely
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (cannot divide by zero)"

# Print results
print("\n--- Results ---")
print(addition)
print(subtraction)
print(multiplication)
print(division)
