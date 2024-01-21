
# for i in range(10):
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(2,10,2):
#     print(i)

# a = input("enter a num")
# print(type(a))


a = int(input("Enter a num"))
c = 0
for i in range(1,a+1):
  if(a % i == 0):
   c = c+1
if c == 2:
    print("prime num")
else:
    print("not prime")        


