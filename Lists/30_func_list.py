# ============================
# PYTHON LISTS - COMPLETE NOTES
# ============================

# Sample Lists
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40, 50]

# 1. append() -> Add one item to the end
fruits.append("orange")

# 2. extend() -> Add multiple items
fruits.extend(["grapes", "kiwi"])

# 3. insert(index, item) -> Insert at specific position
fruits.insert(1, "pear")

# 4. remove(item) -> Remove first occurrence
fruits.remove("banana")

# 5. pop() -> Remove and return item
fruits.pop()        # Removes last item
fruits.pop(0)       # Removes first item

# 6. clear() -> Remove all items
temp = [1, 2, 3]
temp.clear()

# 7. index(item) -> Get position of item
print(numbers.index(30))

# 8. count(item) -> Count occurrences
nums = [1, 2, 2, 3, 2]
print(nums.count(2))

# 9. sort() -> Sort ascending
nums.sort()

# 10. sort(reverse=True) -> Sort descending
nums.sort(reverse=True)

# 11. reverse() -> Reverse list order
nums.reverse()

# 12. copy() -> Create shallow copy
new_nums = nums.copy()

# 13. len() -> Number of elements
print(len(numbers))

# 14. max() -> Largest value
print(max(numbers))

# 15. min() -> Smallest value
print(min(numbers))

# 16. sum() -> Sum of all elements
print(sum(numbers))

# 17. sorted() -> Return new sorted list
new_list = sorted(numbers)

# 18. list() -> Convert iterable to list
letters = list("Python")
print(letters)

# 19. del -> Delete item or entire list
data = [10, 20, 30]
del data[1]
# del data

# 20. in -> Check if item exists
print("apple" in fruits)

# 21. not in -> Check if item does not exist
print("car" not in fruits)

# 22. + -> Concatenate lists
a = [1, 2]
b = [3, 4]
c = a + b
print(c)

# 23. * -> Repeat list
zeros = [0] * 5
print(zeros)

# 24. Slicing
print(numbers[1:4])

# 25. Negative Indexing
print(numbers[-1])

# 26. List Comprehension
squares = [x * x for x in range(6)]
print(squares)

# 27. enumerate() -> Index and value together
for index, value in enumerate(fruits):
    print(index, value)

# 28. zip() -> Combine multiple lists
names = ["Ali", "Ahmed", "Usman"]
ages = [20, 22, 25]

combined = list(zip(names, ages))
print(combined)

# 29. any() -> True if at least one element is True
values = [False, False, True]
print(any(values))

# 30. all() -> True if all elements are True
values = [True, True, True]
print(all(values))


# ======================================
# Actual Python List Methods (11 Methods)
# ======================================

"""
1. append()
2. extend()
3. insert()
4. remove()
5. pop()
6. clear()
7. index()
8. count()
9. sort()
10. reverse()
11. copy()
"""

# ============================
# Quick Example
# ============================

my_list = [10, 20, 30]

my_list.append(40)          # [10, 20, 30, 40]
my_list.insert(1, 15)       # [10, 15, 20, 30, 40]
my_list.remove(20)          # [10, 15, 30, 40]
my_list.pop()               # [10, 15, 30]
my_list.reverse()           # [30, 15, 10]

print(my_list)



# Indexing
# Slicing
# Arithmatic operator
# min , max, len, all, any, count, index 
#  in, append, insert, clear, remove, pop, 
# sort, reverse
# assigment, copy, deepcopy
# + operator, extend, zip, enumerate, map, filter
# comprehension