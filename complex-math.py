
print("Welcome to the Python 2026 Complex Math Program!")

# Ask the user for their name
name = input("Please enter your name: ")
print(f"Hello {name}, let's do some complex Math.")

# Ask the user to choose operations
print("\nChoose one or more math operations (separate with spaces):")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choices = input("Enter your choices (e.g., 1 2 3 4): ").split()

# Get two numbers from the user
num1 = float(input("\nEnter your first number: "))
num2 = float(input("Enter your second number: "))

print("\n--- Results ---")

# Perform ALL selected operations     # In this case, using elif will only print one result no matter how many operations you choose
if "1" in choices:
    print(f"{num1} + {num2} = {num1 + num2}")

if "2" in choices:
    print(f"{num1} - {num2} = {num1 - num2}")

if "3" in choices:
    print(f"{num1} * {num2} = {num1 * num2}")

if "4" in choices:
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(f"{num1} / {num2} = undefined (cannot divide by zero)")
