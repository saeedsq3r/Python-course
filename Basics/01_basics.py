# ==========================================
#            PYTHON BASICS
# ==========================================

"""
Python is a high-level, interpreted, object-oriented,
and easy-to-learn programming language.

Created By : Guido van Rossum
First Released : 1991
Latest Versions : Python 3.x

Features:
✔ Simple Syntax
✔ Easy to Read
✔ Cross Platform
✔ Open Source
✔ Large Community
✔ Object-Oriented
✔ Huge Library Support
"""

# ------------------------------------------
# 1. Printing Output
# ------------------------------------------

print("Hello World!")
print("Welcome to Python")

# Output:
# Hello World!
# Welcome to Python


# ------------------------------------------
# 2. Comments
# ------------------------------------------

# This is a single-line comment

"""
This is
a multi-line
comment.
"""


# ------------------------------------------
# 3. Variables
# ------------------------------------------

name = "Ali"
age = 20
height = 5.8

print(name)
print(age)
print(height)

# Rules:
# ✔ Must start with a letter or underscore
# ✔ Can contain letters, numbers, _
# ✖ Cannot start with a number
# ✖ Cannot use Python keywords


# ------------------------------------------
# 4. Multiple Variable Assignment
# ------------------------------------------

x, y, z = 10, 20, 30

print(x)
print(y)
print(z)


# ------------------------------------------
# 5. Assign Same Value
# ------------------------------------------

a = b = c = 100

print(a, b, c)


# ------------------------------------------
# 6. Data Types
# ------------------------------------------

# Integer
num = 10

# Float
price = 99.99

# String
language = "Python"

# Boolean
is_active = True

# Complex
complex_num = 3 + 4j

print(type(num))
print(type(price))
print(type(language))
print(type(is_active))
print(type(complex_num))


# ------------------------------------------
# 7. Type Casting
# ------------------------------------------

x = "100"

print(int(x))
print(float(x))

y = 50
print(str(y))


# ------------------------------------------
# 8. Getting User Input
# ------------------------------------------

name = input("Enter your name: ")

print("Welcome", name)

# Input always returns a string.


# ------------------------------------------
# 9. Integer Input
# ------------------------------------------

age = int(input("Enter your age: "))

print(age)


# ------------------------------------------
# 10. Float Input
# ------------------------------------------

salary = float(input("Enter your salary: "))

print(salary)


# ------------------------------------------
# 11. Escape Characters
# ------------------------------------------

print("Hello\nWorld")
print("Python\tProgramming")
print("He said \"Hi\"")

# \n -> New Line
# \t -> Tab
# \" -> Double Quote


# ------------------------------------------
# 12. String Concatenation
# ------------------------------------------

first = "Hello"
second = "World"

print(first + " " + second)


# ------------------------------------------
# 13. f-Strings
# ------------------------------------------

name = "Ali"
age = 20

print(f"My name is {name} and I am {age} years old.")


# ------------------------------------------
# 14. Keywords
# ------------------------------------------

import keyword

print(keyword.kwlist)

# To count keywords:
print(len(keyword.kwlist))


# ------------------------------------------
# 15. Identifiers
# ------------------------------------------

student_name = "Ahmed"
_marks = 90

# Valid

# 2name = "Ali"      ❌ Invalid
# class = "Python"   ❌ Keyword


# ------------------------------------------
# 16. Case Sensitive
# ------------------------------------------

name = "Ali"
Name = "Ahmed"

print(name)
print(Name)

# Output:
# Ali
# Ahmed


# ------------------------------------------
# 17. Memory Address
# ------------------------------------------

x = 100

print(id(x))

# id() returns memory location.


# ------------------------------------------
# 18. Multiple Prints
# ------------------------------------------

print("Python", "Java", "C++")

print("2026", "Python", sep="-")

print("Hello", end=" ")
print("World")


# ------------------------------------------
# 19. Constants (Convention)
# ------------------------------------------

PI = 3.14159
MAX_SIZE = 100

# Python does not have true constants.
# Uppercase names are used by convention.


# ------------------------------------------
# 20. Deleting Variables
# ------------------------------------------

x = 10

del x

# print(x)  # NameError


# ------------------------------------------
# 21. Arithmetic Example
# ------------------------------------------

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# ------------------------------------------
# 22. Taking Multiple Inputs
# ------------------------------------------

x, y = input("Enter two numbers: ").split()

print(x)
print(y)


# ------------------------------------------
# 23. Multiple Integer Inputs
# ------------------------------------------

a, b = map(int, input("Enter two numbers: ").split())

print(a + b)


# ------------------------------------------
# 24. Checking Data Type
# ------------------------------------------

value = 100

print(type(value))


# ------------------------------------------
# 25. Boolean Values
# ------------------------------------------

print(True)
print(False)

print(bool(1))
print(bool(0))

# Output:
# True
# False


# ------------------------------------------
# 26. None Type
# ------------------------------------------

data = None

print(data)
print(type(data))


# ------------------------------------------
# 27. Reserved Words Example
# ------------------------------------------

# if = 10      ❌
# while = 20   ❌
# for = 30     ❌

# Keywords cannot be used as variable names.


# ------------------------------------------
# 28. Python File Extension
# ------------------------------------------

"""
Python files use the extension:

.py

Examples:
main.py
app.py
calculator.py
"""


# ------------------------------------------
# 29. Running Python Programs
# ------------------------------------------

"""
Run a Python file:

python filename.py

Example:

python app.py
"""


# ------------------------------------------
# 30. Quick Summary
# ------------------------------------------

"""
Python Basics Summary

✔ print()
✔ input()
✔ Variables
✔ Data Types
✔ type()
✔ id()
✔ Comments
✔ Keywords
✔ Identifiers
✔ Type Casting
✔ f-Strings
✔ Escape Characters
✔ Multiple Assignment
✔ Constants (Convention)
✔ None
✔ bool()

Data Types:
1. int
2. float
3. str
4. bool
5. complex
6. NoneType

Interview Questions:

1. Who created Python?
2. Is Python compiled or interpreted?
3. What is the difference between = and == ?
4. What are Python keywords?
5. What is an identifier?
6. What does input() return?
7. Difference between int(), float(), and str()?
8. What is None?
9. Is Python case-sensitive?
10. What is the use of id() and type()?
"""