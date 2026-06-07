# How to combine two lists in Python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Using the + operator
combined_list = list1 + list2
print("Combined List using + operator:", combined_list)

# Using the extend() method
list1.extend(list2)
print("Combined List using extend() method:", list1)

# Using list comprehension
combined_list_comp = [item for sublist in (list1, list2) for item in sublist]
print("Combined List using list comprehension:", combined_list_comp)

# Using the unpacking operator *
combined_list_unpack = [*list1, *list2]
print("Combined List using unpacking operator *:", combined_list_unpack)

# Using the itertools.chain() method
import itertools
combined_list_chain = list(itertools.chain(list1, list2))
print("Combined List using itertools.chain():", combined_list_chain)

# Using the append() method in a loop
combined_list_loop = []
for item in list1:
    combined_list_loop.append(item)
for item in list2:
    combined_list_loop.append(item)
print("Combined List using append() in a loop:", combined_list_loop)

# Using the numpy library
# import numpy as np
# array1 = np.array(list1)
# array2 = np.array(list2)
# combined_array = np.concatenate((array1, array2))
# print("Combined List using numpy:", combined_array.tolist())

# Using the sum() function  
combined_list_sum = sum([list1, list2], [])
print("Combined List using sum() function:", combined_list_sum)



comb = [list1, list2]
print("Combined List using nested lists:", comb)


# zip to combine two lists into a list of tuples
zipped_list = list(zip(list1, list2))
print("Zipped List:", zipped_list)


# Application of zip function
ids = [101, 102, 103]
names = ['Alice', 'Bob', 'Charlie']

print(list(zip(ids,names)))