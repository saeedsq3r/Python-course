# Access & Read

# Positive Indexing
lst = [10, 20, 30, 40, 50]
print(lst[0])  # Access first element
print(lst[2])  # Access third element


# Negative Indexing
print(lst[-1])  # Access last element
print(lst[-3])  # Access third last element

# Nested List Access
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)  # Print the entire nested list
print(matrix[0][0])  # Access first element of first sub-list
print(matrix[1][2])  # Access third element of second sub-list
print(matrix[2][1])  # Access second element of third sub-list


# slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[2:5])    # Elements from index 2 to 4
print(numbers[:4])     # Elements from start to index 3


# slicing matrix

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(matrix[1:3])        # Slicing rows from index 1 to 2
print(matrix[0][1:3])     # Slicing columns from index 1 to 2 in the first row
print(matrix[2][2:])      # Slicing from index 2 to end in the third row
print(matrix[:2])         # Slicing first two rows
print(matrix[:][1:3])     # Slicing all rows and columns from index 1 to 2
print(matrix[1:3][0][1:3]) # Slicing rows 1 to 2, then slicing columns 1 to 2 of the first sliced row
print(matrix[1:3][1][1:3]) # Slicing rows 1 to 2, then slicing columns 1 to 2 of the second sliced row
print(matrix[:][::2])     # Slicing all rows and every second column
print(matrix[::2])        # Slicing every second row 