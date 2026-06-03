
print("my name is Alice")
print("my name is Bob")
print("my name is Charlie")


# Now Becomes
def student(name):                                  # def = function; greet = name of the function 
    print(f"Hello {name}!")
    print("Welcome to Python")

student("Alice")
student("Bob")
student("Charlie")


# Another example
def student1(name, age):                                  # def = function; greet = name of the function 
    print(f"My name is {name}!")
    print(f"I am {age} years old!")
    print(f"{name}, Welcome to Python")

student1("Alice", 30)
student1("Bob", 46)
student1("Charlie", 60)


# Another example 2
def add(a, b):                                  # def = function; greet = name of the function 
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    

add(20, 30)
add(15, 10)
add(2, 5)