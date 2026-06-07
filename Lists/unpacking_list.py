# unpacking list
person = ['Maria', 28, 'Engineer','Spain']
# name = person[0]
# age = person[1]
# profession = person[2]
# country = person[3]

name, age, profession, country = person

print(name)
print(age)
print(profession)
print(country)


# unpacking with *

name, *details, country = person
print(name)
print(details)
print(country)

name, *details = person

print(name)
print(details)

*details, country = person
print(details)
print(country)

# Underscore _ to ignore values
name, _, profession, _ = person
print(name)
print(profession)


# Undersocre and asterisk combined
name, *_ , country = person
print(name)
print(country)

# unpacking Rules
# 1. The number of variables on the left must match the number of elements 
#    in the list on the right, unless using * to capture multiple elements.
# 2. Only one variable can use the * syntax to capture multiple elements.
# 3. The * variable can be placed anywhere in the variable list.
# 4. The * variable will capture all remaining elements as a list.
# 5. You can use _ as a variable name to ignore specific elements during unpacking.