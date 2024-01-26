def check_prime(number):
  a = int(input("Enter a num"))
  c = 0
  for i in range(1,a+1):
    if(a % i == 0):
     c = c+1
  if c == 2:
     prime = True
  else:
     prime = False  
  return prime    

def print_multiplication_table(number):

    print(f"Multiplication table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

def calculate_f_of_x(x):
    return x**2 + 5*x + 5        


number = int(input("Enter a number: "))

if check_prime(number):
    print(f"{number} is a prime number.")
    print_multiplication_table(number)



else:
    print(f"{number} is not a prime number.")
    result = calculate_f_of_x(number)
    print(f"f({number}) = {result}")




 