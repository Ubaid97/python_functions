# def greeting():
#     print("Welcome")
# Running the code above wouldn't display anything. functions have to called to be executed
# Syntax to call function: greeting()
# Calling a function executes the code it contains


# arguments
# def greeting(name):
#     print(f"Welcome {name}")
#
# greeting("Ubaid")  # function is called by giving an argument


# functions that takes 2 ints as arguments and perform an arithmetic operation on them
def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

# return statement simply returns a value without displaying it.
def divide(num1, num2):
    return(num1 / num2)

def remainder(num1, num2):
    return(num1 % num2)

add(5, 7)
subtract(10, 5)
multiply(7, 8)

# because return statements don't display anything, the last two functions are called in a print function to display the value they return
print(divide(35, 5))
print(remainder(56, 6))