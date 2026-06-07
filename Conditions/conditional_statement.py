# conditional statements in Python
x = 10
if x > 0:
    print("x is positive")


score = 50
submitted_project = True
if score >= 90:
    print("Grade: A")


# two way decision
if score >= 90:
    print("Pass")
else:
    print("Fail")


# multi condition statement
if score >= 90 and submitted_project:
    print("Grade: A+")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70: 
    print("Grade: C")
elif score >= 60 or submitted_project:
    print("Grade: D")
else:
    print("Grade: F")

# conditional operators 
# age = 25
# if age >= 18 and age < 65:
#     print("Adult")

# independent if statements
if score >= 90:
    print("High Score")
else:
    print("Low Score")


if submitted_project:
    print("Project Submitted")
else:
    print("Project Not Submitted")


# ================================= challange =================================

# Validate the Quality and Correctness of Email Values
# email = "saeedsq3r@gmail.com"

# if email != "":
#     if '.'  in email and '@' in email:
#         if email.count('@') == 1:
#             if email.endswith('.com') or email.endswith('.org') or email.endswith('.net'):
#                 if len(email) <= 255:
#                     if email.startswith(email[0]== int(email)) or email.startswith(email[0] == str(email)):
#                         print("correct")
#                     else:
#                         print("incorrect")


email = 'saeedsq3r@gmail.com'
email = email.strip()
valid = True
if email == '':
    print("Email can not be empty.")
    valid = False
if not ('.' in email and '@' in email):
    print("Email must contain . and @")

if email.count('@') != 1:
    print("@ in email must be one")
    valid = False    
if not (email.endswith(('.com','.org','.net'))):
    print("emial must be end with .com or .org or .net")
    valid = False
if len(email) > 255:
    print("Email will no longer then 255 letters.")
    valid = False
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid = False
if valid:
    print("Email is valid")


# validate the Quality and Correctness of Passwords

password = 'saaed+sq3r123'

password = password.strip()
valid = True

if password == '':
    print("password must not be empty")
    valid = False
if not(len(password) >= 8):
    print("password at least 8 characters")
    valid = False
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Password must start and end with a letter or digit")
    valid = False
if not(any([password[0],password[1],password[2],password[3],password[4],password[5],password[6],password[7]]) != password.upper()):
    print("in password at least 1 char be upper case")
    valid = False
if not(any([password[0],password[1],password[2],password[3],password[4],password[5],password[6],password[7]]) != password.lower()):
    print("in password at least 1 char be lower case")
    valid = False
if valid:
    print("password is valid")