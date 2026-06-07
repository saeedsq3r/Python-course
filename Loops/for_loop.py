# ==========================================
#              PYTHON FOR LOOP
# ==========================================

"""
Definition:
A for loop is used to iterate over a sequence
(list, tuple, string, set, dictionary, or range).

Syntax:

for variable in iterable:
    # code block
"""

# ------------------------------------------
# 1. Basic for loop
# ------------------------------------------

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# mango


# ------------------------------------------
# 2. Using range()
# ------------------------------------------

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4


# ------------------------------------------
# 3. range(start, stop)
# ------------------------------------------

for i in range(2, 6):
    print(i)

# Output:
# 2 3 4 5


# ------------------------------------------
# 4. range(start, stop, step)
# ------------------------------------------

for i in range(0, 11, 2):
    print(i)

# Output:
# 0 2 4 6 8 10


# ------------------------------------------
# 5. Loop through a string
# ------------------------------------------

word = "Python"

for letter in word:
    print(letter)

# Output:
# P y t h o n


# ------------------------------------------
# 6. Loop through a tuple
# ------------------------------------------

numbers = (10, 20, 30)

for num in numbers:
    print(num)


# ------------------------------------------
# 7. Loop through a set
# ------------------------------------------

colors = {"red", "green", "blue"}

for color in colors:
    print(color)

# Note:
# Sets are unordered.


# ------------------------------------------
# 8. Loop through a dictionary (Keys)
# ------------------------------------------

student = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}

for key in student:
    print(key)

# Output:
# name
# age
# city


# ------------------------------------------
# 9. Dictionary Values
# ------------------------------------------

for value in student.values():
    print(value)


# ------------------------------------------
# 10. Dictionary Keys and Values
# ------------------------------------------

for key, value in student.items():
    print(key, ":", value)


# ------------------------------------------
# 11. Using break
# ------------------------------------------

for i in range(10):
    if i == 5:
        break
    print(i)

# Stops the loop when i becomes 5.


# ------------------------------------------
# 12. Using continue
# ------------------------------------------

for i in range(6):
    if i == 3:
        continue
    print(i)

# Skips number 3.


# ------------------------------------------
# 13. Using pass
# ------------------------------------------

for i in range(5):
    pass

# pass is a placeholder.


# ------------------------------------------
# 14. Nested for loop
# ------------------------------------------

for i in range(3):
    for j in range(2):
        print(i, j)

# Output:
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1


# ------------------------------------------
# 15. for loop with else
# ------------------------------------------

for i in range(5):
    print(i)
else:
    print("Loop completed successfully.")

# else executes if the loop finishes normally.


# ------------------------------------------
# 16. break with else
# ------------------------------------------

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Finished")

# else will NOT execute because break occurred.


# ------------------------------------------
# 17. enumerate()
# ------------------------------------------

fruits = ["apple", "banana", "mango"]

for index, value in enumerate(fruits):
    print(index, value)

# Output:
# 0 apple
# 1 banana
# 2 mango


# ------------------------------------------
# 18. enumerate(start=1)
# ------------------------------------------

for index, value in enumerate(fruits, start=1):
    print(index, value)

# Output:
# 1 apple
# 2 banana
# 3 mango


# ------------------------------------------
# 19. zip()
# ------------------------------------------

names = ["Ali", "Ahmed", "Usman"]
ages = [20, 21, 22]

for name, age in zip(names, ages):
    print(name, age)


# ------------------------------------------
# 20. Reverse Loop
# ------------------------------------------

for i in range(5, 0, -1):
    print(i)

# Output:
# 5 4 3 2 1


# ------------------------------------------
# 21. Multiplication Table
# ------------------------------------------

num = 5

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# ------------------------------------------
# 22. Sum of Numbers
# ------------------------------------------

total = 0

for i in range(1, 6):
    total += i

print(total)

# Output:
# 15


# ------------------------------------------
# 23. Find Even Numbers
# ------------------------------------------

for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# ------------------------------------------
# 24. Find Odd Numbers
# ------------------------------------------

for i in range(1, 11):
    if i % 2 != 0:
        print(i)


# ------------------------------------------
# 25. Iterate using Index
# ------------------------------------------

fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])


# ------------------------------------------
# 26. List Comprehension (Alternative)
# ------------------------------------------

squares = [x ** 2 for x in range(6)]
print(squares)


# ------------------------------------------
# 27. Infinite Loop? (No)
# ------------------------------------------

# A for loop automatically stops when
# the iterable is exhausted.


# ------------------------------------------
# 28. Common Uses
# ------------------------------------------

# Printing items
# Processing data
# Reading files
# Creating lists
# Working with APIs
# Data analysis


# ------------------------------------------
# 29. Time Complexity
# ------------------------------------------

"""
Single for loop      -> O(n)

Nested for loops     -> O(n²)

Three nested loops   -> O(n³)
"""


# ------------------------------------------
# 30. Quick Summary
# ------------------------------------------

"""
Syntax:
for variable in iterable:
    statements

Keywords:
✔ range()
✔ break
✔ continue
✔ pass
✔ else
✔ enumerate()
✔ zip()

Works with:
✔ List
✔ Tuple
✔ Set
✔ Dictionary
✔ String
✔ Range

Interview Questions:
1. Difference between for and while loop?
2. What does range() return?
3. What is enumerate()?
4. What is zip()?
5. When does else execute in a for loop?
6. Difference between break and continue?
"""