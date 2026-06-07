# sets: Unordered Collection of Unique values.
# Sets: Unordered, No duplicates, Not index , Mutable 

My_set = {10,30,10,20}
print(My_set)


My_set.remove(20)
print(My_set)

# Methods and operator
a = {10, 20, 30, 40}
a.add(50)
print(a)

a.update('Hi')
a.update({1,2})

a |= {1,2}


a.remove(10)

a.discard(50)
a.discard(100)

# a.pop()

print(a)

# Mathematical operator in set

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print(a.difference(b))
print(a - b)
print(b - a)

print(a.symmetric_difference(b))
print(a ^ b)

# Relationship methods
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

print(a.issubset(b))
print(b.issuperset(a))


print(a.isdisjoint(b))
