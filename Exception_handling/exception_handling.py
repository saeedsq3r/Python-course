# =====================================================
#           PYTHON EXCEPTION HANDLING
# =====================================================

"""
Definition:
Exception Handling is used to handle runtime errors
without stopping the execution of the program.

It makes programs more stable and user-friendly.

Syntax:

try:
    # Code that may cause an error
except:
    # Code to handle the error
"""

# -----------------------------------------------------
# 1. Basic try-except
# -----------------------------------------------------

try:
    print(10 / 0)
except:
    print("An error occurred.")

# Output:
# An error occurred.


# -----------------------------------------------------
# 2. Handling Specific Exceptions
# -----------------------------------------------------

try:
    number = int("Python")
except ValueError:
    print("Invalid conversion.")

# Output:
# Invalid conversion.


# -----------------------------------------------------
# 3. Multiple Exceptions
# -----------------------------------------------------

try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# -----------------------------------------------------
# 4. One except for Multiple Errors
# -----------------------------------------------------

try:
    num = int(input("Enter a number: "))
    print(10 / num)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")


# -----------------------------------------------------
# 5. Exception as Object
# -----------------------------------------------------

try:
    print(10 / 0)

except Exception as e:
    print("Error:", e)

# Output:
# Error: division by zero


# -----------------------------------------------------
# 6. else Block
# -----------------------------------------------------

"""
The else block executes only if
no exception occurs.
"""

try:
    num = int(input("Enter a number: "))
    print(num)

except ValueError:
    print("Invalid Input")

else:
    print("Program executed successfully.")


# -----------------------------------------------------
# 7. finally Block
# -----------------------------------------------------

"""
The finally block always executes,
whether an exception occurs or not.
"""

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Error")

finally:
    print("Program Finished")


# -----------------------------------------------------
# 8. Complete Structure
# -----------------------------------------------------

try:
    print(10 / 5)

except Exception:
    print("Error")

else:
    print("No Error")

finally:
    print("Always Execute")


# -----------------------------------------------------
# 9. Raising Exceptions
# -----------------------------------------------------

raise Exception("Something went wrong.")

# Output:
# Exception: Something went wrong.


# -----------------------------------------------------
# 10. Raise ValueError
# -----------------------------------------------------

age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")


# -----------------------------------------------------
# 11. User Defined Exception
# -----------------------------------------------------

class InvalidAgeError(Exception):
    pass

age = -1

if age < 0:
    raise InvalidAgeError("Invalid Age")


# -----------------------------------------------------
# 12. Handling User Defined Exception
# -----------------------------------------------------

class MarksError(Exception):
    pass

try:
    marks = -10

    if marks < 0:
        raise MarksError("Marks cannot be negative.")

except MarksError as e:
    print(e)


# -----------------------------------------------------
# 13. File Exception Example
# -----------------------------------------------------

try:
    file = open("data.txt", "r")

except FileNotFoundError:
    print("File does not exist.")


# -----------------------------------------------------
# 14. IndexError Example
# -----------------------------------------------------

try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Invalid Index")


# -----------------------------------------------------
# 15. KeyError Example
# -----------------------------------------------------

try:
    student = {
        "name": "Ali"
    }

    print(student["age"])

except KeyError:
    print("Key Not Found")


# -----------------------------------------------------
# 16. TypeError Example
# -----------------------------------------------------

try:
    print("10" + 10)

except TypeError:
    print("Type Mismatch")


# -----------------------------------------------------
# 17. NameError Example
# -----------------------------------------------------

try:
    print(x)

except NameError:
    print("Variable not defined.")


# -----------------------------------------------------
# 18. AttributeError Example
# -----------------------------------------------------

try:
    num = 10
    num.append(5)

except AttributeError:
    print("Invalid Attribute")


# -----------------------------------------------------
# 19. ImportError Example
# -----------------------------------------------------

try:
    import unknown_module

except ImportError:
    print("Module not found.")


# -----------------------------------------------------
# 20. AssertionError
# -----------------------------------------------------

try:
    x = 5

    assert x > 10

except AssertionError:
    print("Assertion Failed")


# -----------------------------------------------------
# 21. Nested try-except
# -----------------------------------------------------

try:

    try:
        print(10 / 0)

    except ZeroDivisionError:
        print("Inner Exception")

except:
    print("Outer Exception")


# -----------------------------------------------------
# 22. Catch All Exceptions
# -----------------------------------------------------

try:
    x = int("Python")

except Exception:
    print("Something went wrong.")


# -----------------------------------------------------
# 23. Using pass
# -----------------------------------------------------

try:
    print(10 / 0)

except ZeroDivisionError:
    pass

print("Program Continues")


# -----------------------------------------------------
# 24. Logging Exception
# -----------------------------------------------------

try:
    print(10 / 0)

except Exception as e:
    print(f"Error Type: {type(e).__name__}")
    print(f"Message: {e}")


# -----------------------------------------------------
# 25. Custom Validation
# -----------------------------------------------------

password = "123"

try:

    if len(password) < 6:
        raise ValueError("Password too short.")

except ValueError as e:
    print(e)


# -----------------------------------------------------
# 26. Common Built-in Exceptions
# -----------------------------------------------------

"""
ValueError
TypeError
NameError
IndexError
KeyError
AttributeError
ImportError
FileNotFoundError
ZeroDivisionError
AssertionError
RuntimeError
MemoryError
OverflowError
EOFError
"""


# -----------------------------------------------------
# 27. Why Use Exception Handling?
# -----------------------------------------------------

"""
✔ Prevents program crashes.
✔ Improves user experience.
✔ Makes debugging easier.
✔ Handles unexpected situations.
"""


# -----------------------------------------------------
# 28. Best Practices
# -----------------------------------------------------

"""
✔ Catch specific exceptions.
✔ Use finally for cleanup.
✔ Use with for file handling.
✔ Avoid empty except blocks.
✔ Create custom exceptions when needed.
"""


# -----------------------------------------------------
# 29. Flow of Exception Handling
# -----------------------------------------------------

"""
try
 ↓
Exception?
 ↓         ↓
Yes        No
 ↓          ↓
except     else
 ↓          ↓
    finally
"""


# -----------------------------------------------------
# 30. Quick Summary
# -----------------------------------------------------

"""
Keywords:

✔ try
✔ except
✔ else
✔ finally
✔ raise
✔ pass

Basic Syntax:

try:
    statements

except ExceptionType:
    statements

else:
    statements

finally:
    statements

Common Exceptions:

✔ ValueError
✔ TypeError
✔ NameError
✔ IndexError
✔ KeyError
✔ AttributeError
✔ ImportError
✔ FileNotFoundError
✔ ZeroDivisionError

Interview Questions:

1. What is an exception?
2. What is the difference between syntax errors and exceptions?
3. What is the purpose of try and except?
4. When does else execute?
5. When does finally execute?
6. What is the use of raise?
7. How do you create a custom exception?
8. Difference between Exception and BaseException?
9. Why should we catch specific exceptions?
10. What are the best practices for exception handling?
"""