# ==========================================
#        PYTHON SWITCH (match-case)
# ==========================================

"""
Definition:
Python does not have a traditional switch statement
like C, C++, or Java.

Starting from Python 3.10, Python introduced
Structural Pattern Matching using 'match-case',
which works similarly to a switch statement.

Syntax:

match expression:
    case value1:
        # code
    case value2:
        # code
    case _:
        # Default case
"""

# ------------------------------------------
# 1. Basic match-case
# ------------------------------------------

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")

# Output:
# Tuesday


# ------------------------------------------
# 2. Default Case (_)
# ------------------------------------------

color = "yellow"

match color:
    case "red":
        print("Red Color")
    case "green":
        print("Green Color")
    case _:
        print("Unknown Color")

# Output:
# Unknown Color


# ------------------------------------------
# 3. Matching Strings
# ------------------------------------------

fruit = "apple"

match fruit:
    case "apple":
        print("Apple Selected")
    case "banana":
        print("Banana Selected")
    case _:
        print("No Match")


# ------------------------------------------
# 4. Matching Numbers
# ------------------------------------------

number = 100

match number:
    case 50:
        print("Fifty")
    case 100:
        print("One Hundred")
    case _:
        print("Other Number")


# ------------------------------------------
# 5. Multiple Values in One Case (|)
# ------------------------------------------

letter = "a"

match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant")


# ------------------------------------------
# 6. User Input Example
# ------------------------------------------

choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You selected One")
    case 2:
        print("You selected Two")
    case 3:
        print("You selected Three")
    case _:
        print("Invalid Choice")


# ------------------------------------------
# 7. Match with Conditions (Guard)
# ------------------------------------------

age = 18

match age:
    case x if x >= 18:
        print("Adult")
    case _:
        print("Minor")

# Output:
# Adult


# ------------------------------------------
# 8. Matching Lists
# ------------------------------------------

data = [1, 2]

match data:
    case [1, 2]:
        print("Matched List")
    case _:
        print("No Match")


# ------------------------------------------
# 9. Matching Tuples
# ------------------------------------------

point = (10, 20)

match point:
    case (10, 20):
        print("Point Found")
    case _:
        print("Unknown Point")


# ------------------------------------------
# 10. Matching Dictionaries
# ------------------------------------------

student = {
    "name": "Ali",
    "age": 20
}

match student:
    case {"name": name, "age": age}:
        print(f"Name: {name}, Age: {age}")
    case _:
        print("No Match")


# ------------------------------------------
# 11. Multiple Statements
# ------------------------------------------

grade = "A"

match grade:
    case "A":
        print("Excellent")
        print("Keep it up!")
    case "B":
        print("Good")
    case _:
        print("Try Again")


# ------------------------------------------
# 12. Calculator Example
# ------------------------------------------

operator = "+"

match operator:
    case "+":
        print(10 + 5)
    case "-":
        print(10 - 5)
    case "*":
        print(10 * 5)
    case "/":
        print(10 / 5)
    case _:
        print("Invalid Operator")


# ------------------------------------------
# 13. Simple Menu Program
# ------------------------------------------

menu = 2

match menu:
    case 1:
        print("Home")
    case 2:
        print("Profile")
    case 3:
        print("Settings")
    case _:
        print("Exit")


# ------------------------------------------
# 14. Nested match-case
# ------------------------------------------

category = "fruit"
item = "apple"

match category:
    case "fruit":
        match item:
            case "apple":
                print("Apple Fruit")
            case "banana":
                print("Banana Fruit")
    case _:
        print("Unknown Category")


# ------------------------------------------
# 15. Traditional Alternative (Dictionary)
# ------------------------------------------

def monday():
    return "Monday"

def tuesday():
    return "Tuesday"

switch = {
    1: monday,
    2: tuesday
}

print(switch.get(2, lambda: "Invalid")())

# Before Python 3.10, this was commonly used.


# ------------------------------------------
# 16. Important Notes
# ------------------------------------------

"""
1. match-case was introduced in Python 3.10.
2. The '_' symbol acts as the default case.
3. '|' works like OR.
4. Guards use 'if'.
5. Works with:
   ✔ Numbers
   ✔ Strings
   ✔ Lists
   ✔ Tuples
   ✔ Dictionaries
   ✔ Objects
"""


# ------------------------------------------
# 17. Advantages
# ------------------------------------------

"""
✔ Cleaner than many if-elif statements.
✔ Easier to read.
✔ Supports pattern matching.
✔ Good for menus and command handling.
"""


# ------------------------------------------
# 18. Limitations
# ------------------------------------------

"""
✖ Only available in Python 3.10+.
✖ Simple if-else is often enough for small programs.
"""


# ------------------------------------------
# 19. if-elif vs match-case
# ------------------------------------------

"""
if-elif:

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
else:
    print("Invalid")


match-case:

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")
"""


# ------------------------------------------
# 20. Quick Summary
# ------------------------------------------

"""
Syntax:

match expression:
    case value1:
        statements
    case value2:
        statements
    case _:
        default statements

Keywords:
✔ match
✔ case
✔ _
✔ |
✔ if (Guard)

Interview Questions:
1. Does Python have a switch statement?
2. What is match-case?
3. Which Python version introduced match-case?
4. What does '_' represent?
5. What is the purpose of '|' in match-case?
6. What are Guards in pattern matching?
"""