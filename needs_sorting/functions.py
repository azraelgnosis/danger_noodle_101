# some built in functions
print("Hello World!")

nums = list(3, 6, 87, -435)
max_nums = max(nums)
print(max_nums)
print(sorted(nums))
print(nums)
print(pow(4, 3))

def greet():
    """
    Prints the string "Hey, there"
    """
    
    print("Hey, there")

greet()

def increment(x):
    print(x+1)

increment(5)

def increment(x):
    plus_one = x + 1

    return plus_one

x = 7
x = increment(x)

def add(a, b):
    return a+b

y = add(3, 6)
print(y)