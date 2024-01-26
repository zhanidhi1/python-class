def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_multiplication_table(number):

    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
    print_multiplication_table(number)
else:
    print(f"{number} is not a prime number.")