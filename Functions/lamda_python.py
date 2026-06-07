#  lambda or anonymous function is a small anonymous function that 
# can take any number of arguments,
#  but can only have one expression.


# Syntax: lambda arguments: expression

multiply = lambda x: x * 10

print(multiply(5))  # Output: 50


add = lambda x, y: x + y

print(add(3, 7))  # Output: 10 


check = lambda i: i in "python"

print(check('y'))  # Output: True
print(check('z'))  # Output: False


# Application
prices = ['$5.00', '$10.00', '$7.50', '$3.25']
print(list(map(lambda p: float(p.replace('$', '')), prices)))

# lambda + filter

prices = [120, 75, 200, 50, 300, 90]
print(list(filter(lambda p: p >= 100, prices)))


students = [
    ['Mria', 85],
    ['Alice', 92],
    ['Bob', 78],
    ['Max', 90]
]

# print(list(filter(lambda row: row[1] > 85, students)))
print(list(filter(lambda row: row[0].startswith('M') and row[1] >= 85, students)))


# sort list

