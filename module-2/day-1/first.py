#List
a = [1,2,3,4,5,"hello",True]
print(type(a))
b = [1,2,3,4,5,"hello",True]
print(type(b))
print(a[3])
print(a[-3])

#append/add garne
a.append('Nidhi')
print(a)

#append lai delete garne
a.pop()
print(a)

#index (data ko position thah paune)
print(a.index(5))

a.insert(3, True)
print(a.insert)

print(a)

a.insert(3, 'Jha')
print(a.insert)
print(a)

a.index(3)
print(a.index)
a.insert(a.index(3), False)
print(a.insert)
print(a)

a.insert(4, "happy")
print(a.insert)
print(a)

a.pop()
print(a)

a.remove(4)
print(a.remove)
print(a)

a.reverse()
print(a)

a.index(5)
print(a)

a[1:5]
print(a)

b=a[1:5]
print(b)

b=a[2:-1]
print(b)

a.reverse()
print(a)

a[-2:5]
print(a)

a[4:]
print(a)


a[:3:5]
print(a)
# find even index
a[: :2]
print(a)

 # find odd index
a[::2]

a[: :-1]
print(a)

#count the number of element
print(a.count(2))

sor = [2,4,1,5,3,6,4,7]
sor.sort()
print(sor)

b = sor
b.sort()
print(b)

b=sor.copy()
b.sort()
print(b)


