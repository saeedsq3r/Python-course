# coping list
original_list = [1, 2, 3, 4, 5]
# Creating a shallow copy of the list
copied_list = original_list.copy()
print("Original List:", original_list)
print("Copied List:", copied_list)
# Modifying the copied list
copied_list.append(6)
print("Modified Copied List:", copied_list)
print("Original List after modifying Copied List:", original_list)

# Creating a deep copy of a nested list
import copy
nested_list = [[1, 2], [3, 4]]
deep_copied_list = copy.deepcopy(nested_list)
print("Nested List:", nested_list)
print("Deep Copied List:", deep_copied_list)


matrix = [
    ['a','b'],
    ['c','d']
]

matrix_copy = copy.copy(matrix)


# Check Two Vaeriables reger to the same object

copy1 = original_list
print("Same Object?", original_list is copy1)  # True

# Shallow copy
copy2 = original_list.copy()
print("Same Object?", original_list is copy2)  # False
print("Shared Lists?", original_list[0] is copy2[0], "\n")  # False


# Deep copy
copy3 = copy.deepcopy(original_list)
print("Same Object?", original_list is copy3)  # False
print("Shared Lists?", original_list[0] is copy3[0])  # False