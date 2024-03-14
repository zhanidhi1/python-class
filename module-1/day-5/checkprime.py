def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_f_of_x(x):
    return x**2 + 5*x + 2

def print_multiplication_table(number):

    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
    result = calculate_f_of_x(number)
    print(f"f({number}) = {result}")
else:
    print(f"{number} is not a prime number.")
    print_multiplication_table(number)



def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_f_of_x(x):
    return x**2 + 5*x + 2

def print_multiplication_table(number):

    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
    result = calculate_f_of_x(number)
    print(f"f({number}) = {result}")
else:
    print(f"{number} is not a prime number.")
    print_multiplication_table(number)    