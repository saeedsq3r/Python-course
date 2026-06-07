# Iterator vs Iterable in Python
# An Iterable is any Python object capable of returning its members one at a time,
# allowing it to be iterated over in a for-loop. 
# Examples include lists, tuples, strings, and dictionaries.
# An Iterator is an object that represents a stream of data; 
# it returns the next item from

# letters = ['a', 'b', 'c']

# new_list = []
# for l in letters:
#     new_list.append(l.upper())
#     print(new_list)


# Iterators enumorate reveresed zip

letters = ['a', 'b', 'c']

# for index, value in enumerate(letters):
#     print(f"Index: {index}, Value: {value}")


letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

# for l in reversed(letters):
#     print(l)    


# print(list(zip(letters, numbers)))
# for pair in zip(letters, numbers):
#     print(pair)


# Iterator map

letters = ['a', 'b', 'c']

print(list(map(str.upper, letters)))

numbers = ['1', '2', '3']
print(list(map(int, numbers)))

names = ['  Maria ', 'john ', ' Alice']

print(list(map(str.strip, names)))


for n in map(str.strip, names):
    print(n)


# Iterator filter
leeters = ['a', '', 'b', None, 'c', False]
print(list(filter(None, leeters)))



print(list(filter(bool, leeters)))


items = ['sql', '123', 'python', '42']

print(list(filter(str.isalpha, items)))

for i in filter(str.isalpha, items):
    print(i)