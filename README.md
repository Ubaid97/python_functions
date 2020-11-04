# Functions
### Why are functions useful?
### Best practices
- **DRY - Don't Repeat Yourself** 
- small block of codes
- pseudo-coding - max one line 
- comments explaning function results
### How to create a function
````
def name_of_function():
    code
````
### Running functions
- A functions must be called in order to be executed
````
def greeting():
    print("Welcome")
    
greeting()
````
- functions can take arguments:
````
def greeting(name):
    print(f"Welcome {name}")

greeting("Ubaid")
````
- Return statement simply returns a value without displaying it. also the last line of function that runs
````
def divide(num1, num2):
    return(num1 / num2)

print(divide(35, 5))
````