#Most important for interview
# odd even in list
# A = [1,2,3,4,5,6,7,8,9,12,11]
# even_list, odd_list = [],[]
# for element in A:
#     if element % 2 ==0:
#         even_list.append(element)
#     else:
#         odd_list.append(element)    
# print("Even numbers:", even_list)
# print("Odd numbers:", odd_list)

#output
#Even numbers: [2, 4, 6, 8, 12]
#Odd numbers: [1, 3, 5, 7, 9, 11]


#List comprihension
# A = [1,2,3,5,56,6,7,7,77,7,5,4,4,3,2,2,2]
# C = [element+3 for element in A]
# print(C)

# result = [element for element in A if element%2 == 0]
# print(result)

# result1 = [element for element in A if element%2 != 0]
# print(result1)


a = [-1,2,-3,5,-4,8,-7,9,-10,11,-23,24]
b = [element for element in a if element>0]
print(b)
c= [element for element in a if element<0]
print(c)

print(len(b))
print(len(c))
