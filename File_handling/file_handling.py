# =====================================================
#              PYTHON FILE HANDLING
# =====================================================

"""
Definition:
File Handling is used to create, read, write,
append, and manage files.

Python provides the open() function for working
with files.

Syntax:

file = open("filename", "mode")
"""

# -----------------------------------------------------
# 1. File Modes
# -----------------------------------------------------

"""
'r'   -> Read (Default)
'w'   -> Write (Creates new file if not exists)
'a'   -> Append
'x'   -> Create new file
'r+'  -> Read and Write
'w+'  -> Write and Read
'a+'  -> Append and Read
'rb'  -> Read Binary
'wb'  -> Write Binary
'ab'  -> Append Binary
"""

# -----------------------------------------------------
# 2. Open a File
# -----------------------------------------------------

file = open("sample.txt", "r")

# Always close the file after use.
file.close()


# -----------------------------------------------------
# 3. Read Entire File
# -----------------------------------------------------

file = open("sample.txt", "r")

print(file.read())

file.close()


# -----------------------------------------------------
# 4. Read Specific Characters
# -----------------------------------------------------

file = open("sample.txt", "r")

print(file.read(10))

file.close()


# -----------------------------------------------------
# 5. readline()
# -----------------------------------------------------

file = open("sample.txt", "r")

print(file.readline())
print(file.readline())

file.close()


# -----------------------------------------------------
# 6. readlines()
# -----------------------------------------------------

file = open("sample.txt", "r")

print(file.readlines())

file.close()


# -----------------------------------------------------
# 7. Loop Through a File
# -----------------------------------------------------

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()


# -----------------------------------------------------
# 8. Write to a File
# -----------------------------------------------------

file = open("sample.txt", "w")

file.write("Hello Python!")

file.close()

# Existing content will be overwritten.


# -----------------------------------------------------
# 9. Write Multiple Lines
# -----------------------------------------------------

file = open("sample.txt", "w")

lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

file.writelines(lines)

file.close()


# -----------------------------------------------------
# 10. Append Data
# -----------------------------------------------------

file = open("sample.txt", "a")

file.write("\nWelcome to File Handling")

file.close()


# -----------------------------------------------------
# 11. Create a New File
# -----------------------------------------------------

file = open("newfile.txt", "x")

file.close()

# Error if file already exists.


# -----------------------------------------------------
# 12. with Statement
# -----------------------------------------------------

"""
Best practice for file handling.
Automatically closes the file.
"""

with open("sample.txt", "r") as file:
    print(file.read())


# -----------------------------------------------------
# 13. Check if File Exists
# -----------------------------------------------------

import os

if os.path.exists("sample.txt"):
    print("File Exists")
else:
    print("File Not Found")


# -----------------------------------------------------
# 14. Delete a File
# -----------------------------------------------------

import os

if os.path.exists("sample.txt"):
    os.remove("sample.txt")


# -----------------------------------------------------
# 15. Rename a File
# -----------------------------------------------------

import os

os.rename("old.txt", "new.txt")


# -----------------------------------------------------
# 16. Get Current Position
# -----------------------------------------------------

file = open("sample.txt", "r")

print(file.tell())

file.close()


# -----------------------------------------------------
# 17. Move Cursor (seek)
# -----------------------------------------------------

file = open("sample.txt", "r")

file.seek(5)

print(file.read())

file.close()


# -----------------------------------------------------
# 18. Read and Write (r+)
# -----------------------------------------------------

file = open("sample.txt", "r+")

print(file.read())

file.write("\nPython")

file.close()


# -----------------------------------------------------
# 19. Write and Read (w+)
# -----------------------------------------------------

file = open("sample.txt", "w+")

file.write("Hello")

file.seek(0)

print(file.read())

file.close()


# -----------------------------------------------------
# 20. Append and Read (a+)
# -----------------------------------------------------

file = open("sample.txt", "a+")

file.write("\nWelcome")

file.seek(0)

print(file.read())

file.close()


# -----------------------------------------------------
# 21. Binary Write
# -----------------------------------------------------

file = open("image.bin", "wb")

data = bytes([65, 66, 67])

file.write(data)

file.close()


# -----------------------------------------------------
# 22. Binary Read
# -----------------------------------------------------

file = open("image.bin", "rb")

print(file.read())

file.close()


# -----------------------------------------------------
# 23. File Properties
# -----------------------------------------------------

file = open("sample.txt", "r")

print(file.name)
print(file.mode)
print(file.closed)

file.close()


# -----------------------------------------------------
# 24. CSV File Example
# -----------------------------------------------------

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age"])
    writer.writerow(["Ali", 20])


# -----------------------------------------------------
# 25. Read CSV File
# -----------------------------------------------------

import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# -----------------------------------------------------
# 26. JSON Write Example
# -----------------------------------------------------

import json

student = {
    "name": "Ali",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file)


# -----------------------------------------------------
# 27. JSON Read Example
# -----------------------------------------------------

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)


# -----------------------------------------------------
# 28. Common Errors
# -----------------------------------------------------

"""
FileNotFoundError
PermissionError
IsADirectoryError
UnicodeDecodeError
"""


# -----------------------------------------------------
# 29. Advantages of with Statement
# -----------------------------------------------------

"""
✔ Automatically closes files.
✔ Cleaner code.
✔ Prevents resource leaks.
✔ Handles exceptions better.
"""


# -----------------------------------------------------
# 30. Quick Summary
# -----------------------------------------------------

"""
File Handling Functions:

✔ open()
✔ close()
✔ read()
✔ readline()
✔ readlines()
✔ write()
✔ writelines()
✔ seek()
✔ tell()

File Modes:

r   -> Read
w   -> Write
a   -> Append
x   -> Create
r+  -> Read + Write
w+  -> Write + Read
a+  -> Append + Read
rb  -> Read Binary
wb  -> Write Binary
ab  -> Append Binary

Useful Modules:

✔ os
✔ csv
✔ json

Best Practice:

with open("file.txt", "r") as file:
    data = file.read()

Interview Questions:

1. What is file handling?
2. What is the difference between r, w, and a modes?
3. What is the advantage of using with?
4. Difference between read(), readline(), and readlines()?
5. What do seek() and tell() do?
6. Difference between text and binary files?
7. How do you check if a file exists?
8. How do you delete or rename a file?
9. How do you work with CSV files?
10. How do you work with JSON files?
"""