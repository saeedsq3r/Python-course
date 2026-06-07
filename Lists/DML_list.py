# Add, Remove, and Update items in a list

# Adding items
my_list = [10, 20, 30]
print("Original List:", my_list)
my_list.append(40)
print("After appending 40:", my_list)
my_list.extend([50, 60])
print("After extending with [50, 60]:", my_list)
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

# Removing items
my_list.remove(15)
print("After removing 15:", my_list)
popped_item = my_list.pop()
print("Popped item:", popped_item)
print("After popping last item:", my_list)

# Updating items
my_list[2] = 25
print("After updating index 2 to 25:", my_list)

# Now in matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original Matrix:", matrix)
matrix[1][1] = 55
print("After updating matrix[1][1] to 55:", matrix)
matrix.append([10, 11, 12])
print("After appending [10, 11, 12]:", matrix)
matrix[0].remove(2)
print("After removing 2 from first row:", matrix)
matrix.insert(2, [13, 14, 15])
print("After inserting [13, 14, 15] at index 2:", matrix)

# Removing
removed_row = matrix.pop(3)
print("Removed row:", removed_row)
matrix.remove([7, 8, 9])
print("After removing [7, 8, 9]:", matrix)

# updating
matrix[0][0] = 99
print("After updating matrix[0][0] to 99:", matrix)
matrix[1] = [20, 21, 22]
print("After updating second row to [20, 21, 22]:", matrix)


# Clearing a list
my_list.clear()
print("After clearing the list:", my_list)
