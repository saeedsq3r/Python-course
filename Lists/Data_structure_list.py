# data structure: list[],tuple(),set{},dictionary{}
# tuple: ordered,immutable,allows duplicate elements
# set: unordered,mutable,does not allow duplicate elements
# dictionary: unordered,mutable,key-value pairs,keys are unique


# list: ordered,mutable,allows duplicate elements

empty = []
print(type(empty))
fruits = ['apple', 'banana', 'cherry', 'apple']
print(type(fruits))

letters= ['a', 'b', 'c']
print(letters)

numbers = [1, 2, 3, 4, 5]
print(numbers)

mixed = [1, 'hello', 3.14, True,None]
print(mixed)

empty = list()
print(empty)
letters = 'Python'
print(list(letters))

numbers = list(range(1,6))
print(numbers)

# nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

mixed_matrix = [
    [1, 'a', True],
    [3.14, None, 'hello']
]
print(mixed_matrix)

