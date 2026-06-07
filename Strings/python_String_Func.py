################################### Types Functions in Python ###################################
# type Fucntion
name = 'Muhammad'
print(type(name))  # Output: <class 'str'>

age = 24
print(type(age))  # Output: <class 'int'>

# ========================================================

# str() Function
print("Your Age is:" + str(age))  # Converting int to str for concatenation

################################### Math Functions in Python ###################################

# len() Function
password = "P@ssw0rd123"
print(len(password))  # Output: 11

if len(password) < 8:
    print("Your password is too short.")

# .count() Method

text = """
Python is earsy to learn.
Python is powerful.
Many people love Python.

"""

print(text.count("Python"))  # Output: 3

################################### Transformations Functions in Python ###################################

# replace() Method
price = "1234,56"
print(price.replace(",", "."))  # Output: 1234.56

phone = "0123-456-789"
print(phone.replace("-", "/"))  # Output: 0123/456/789

price2 = "$1,299.99"
print(price2.replace("$", "").replace(",", ""))  # Output: 1299.99

# ======================= python Challenge =======================
phone = "+49 (176) 123-4567"

cleaned_phone = phone.replace(
    "+", "00").replace("(", "").replace("-", "").replace(")", "").replace(" ", "")
print(cleaned_phone)


# join (Concatenates) two string into one
first_name = "Muhammad"
last_name = "Awais"
last_name = first_name + " " + last_name
print(last_name)  # Output: Muhammad Awais


folder = "C:/Users/Muhammad/Documents/"
file = "file.txt"
full_file_path = folder + file
print(full_file_path)  # Output: C:/Users/Muhammad/Documents/file.txt

# f-string (Formatted String)
name = 'Muhammad'
age = 24
is_student = True
print(f'Hello, My name is {name}. I am {age} years old. Student Status {is_student}')

# python split Function
info = "Adam-05-USA"
name, month, country = info.split("-")
print(f'Name: {name}')     # Output: Adam
print(f'Month: {month}')    # Output: 05
print(f'Country: {country}')  # Output: USA
# Transformations
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))  # Output: ['1234', 'Max', 'USA', '1970-10-05', 'M']

# multiply operater
print("Ha" * 3)  # Output: HaHaHa

# Indexing and Slicing
language = "Python"
print(language[0])    # Output: P
print(language[-1])   # Output: n
# slicing
print(language[1:4])  # Output: yth
print(language[:3])   # Output: Pyt

# Cleaning up the string values
# clean whitespaces
user_input = "   Hello, World!   "
print(user_input.strip())  # Output: Hello, World!
# clean special characters
data = "***Important Message***"
print(data.strip("*"))  # Output: Important Message
# clean both sides
data2 = "   ###Welcome###   "
print(data2.strip().strip("#"))  # Output: Welcome
# Challenge
raw_data = "   $$$$Special Offer!!!$$$$   "
print(raw_data.strip().strip("$").rstrip("!"))  # Output: Special Offer
# left whitespaces
user_input2 = "   Hello, Python!   "
print(user_input2.lstrip())  # Output: "Hello, Python!   "
# right whitespaces
user_input3 = "   Hello, Python!   "
print(user_input3.rstrip())  # Output: "   Hello, Python!"

# scenario
text = "  Enineering"
print(len(text))  # Output: 12
print(len(text.strip()))  # Output: 10

nr_of_spces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print(f"Nr of spaces: {nr_of_spces}")  # Output: Nr of spaces: 2
print(f"Is the text clean? {is_clean}")  # Output: Is the text


# clean the cases conversion
messy_string = "pYtHoN ProGRamMing"
print(messy_string.lower())  # Output: python programming
print(messy_string.upper())  # Output: PYTHON PROGRAMMING

# scenario
search = "Email  ".lower().strip()
data = '  emAil'.lower().strip()
print(search == data)  # Output: True

# challenge
text = "968-Maria, ( D@t@ Engineer );; 27y  "
cleaned_text = text.strip().replace("@",'a').replace(";;",'').replace("( ",'').replace(" )",'')
print(cleaned_text)  

x, y, z, w = cleaned_text.split(" ")


print(f"name: {x.split('-')[1].strip(',')} | role: {y+z} | age: {w.strip('y')}") 

# Search operator
phone = '+49-176-12345'
print(phone.startswith('+49'))

email = "saeedsq3r@gmail.com"
print(email.endswith('gmail.com'))


file = 'data_backup.csv'
print(file.endswith('.csv'))

print('@' in email)

url = 'http://api.www.example.com'
print('api' in url)

# use of find() method
phone1 = '49-234-5678'
phone2 = '49-176-12345'
print(phone1[phone1.find('-')+1:])
print(phone2[phone2.find('-')+1:])
print(phone1.find('-'))

# string validating
username = "User_123"
print(username.isalnum())  # Output: True
password = "Pass@123"
print(password.isalnum())  # Output: False
code = "ABC123"
print(code.isalpha())  # Output: False
word = "Hello"
print(word.isalpha())  # Output: True
digit_str = "2024"
print(digit_str.isdigit())  # Output: True
# isnumeric() method
numeric_str = "12345"
print(numeric_str.isnumeric())  # Output: True
float_str = "123.45"
print(float_str.isnumeric())  # Output: False