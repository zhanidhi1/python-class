# def check_prime(number):
#  a = int(input("Enter a num"))
#  c = 0
#  for i in range(1,a+1):
#    if(a % i == 0):
#     c = c+1
#  if c == 2:
#      print("prime num")
#  else:
#      print("not prime")
# number = input("Enter a number to check prime")
# check_prime_bool = check_prime(number)

# if check_prime_bool:
#   print("Prime number")  
# else:
#   print("Not Prime number")  

#multiplication table
# def print_multiplication_table(number):
#     for i in range(1, 11):
#         result = number * i
#         print(f"{number} x {i} = {result}")


# user_input = input("Enter a number: ")


# try:
#     number = int(user_input)
#     print_multiplication_table(number)
# except ValueError:
#     print("Please enter a valid number.")


def get_multiplication_table(num):
     for i in range(1, 11):
         print(f"{num} * {i} = {num*i}")
         #         5   *  1  = 5
         #         5   *  2  = 10
number = int(input("Enter a number")) 
get_multiplication_table(number) 


