# Logical operatos
print(3 > 1 and 5 < 10)
print(3 > 1 or 5 > 10)
print(not (3 > 1))

# Check if a number is even and positive
number = 4
is_even_and_positive = (number % 2 == 0) and (number > 0)
print(is_even_and_positive)

print(3 > 1 or 5 > 10)
print(not (3 > 1))
print((3 > 1) or (5 < 10))

# Check if the system is under pressure
cpu_usage = 85  # in percentage
memory_usage = 70  # in percentage
is_under_pressure = (cpu_usage > 80) and (memory_usage > 75)
print(is_under_pressure)
# Check if a user can access a resource
user_role = "admin"
is_admin = (user_role == "admin") or (user_role == "superuser")
print(is_admin)


# check user cridentials before login
username = "user1"
password = "pass123"
is_valid_user = (username == "user1") and (password == "pass123")
print(is_valid_user)


# the not operator
is_guest_user = True
can_access_limited_features = not is_guest_user
print(can_access_limited_features)

# Allow acces only if the user is logged in
# or they are a guest
# but they must not be banned


is_logged_in = False
is_guest = True
is_banned = True


print((is_logged_in or is_guest) and not is_banned)

# ==================================================== challenge ====================================================
# 1. Check if a user's name is not empty and the age is greater than or equal to 18.
user_name = "Alice"
user_age = 20
print(user_name != "" and (user_age > 18 or user_age == 18))

# 2. Check if the password is at least 8 characters long and does not conatin spaces.
password = "securePass"
print(len(password) >= 8 and " " not in password)

# 3. Check if a user's email is not empty, contains '@', and ends with '.com'
user_email = 'saeed@gmail.com'
print(len(user_email) != '' and '@' in user_email and user_email.endswith('.com'))

# 4. Check if a username is a string, is not None, and is longer than 5 characters
username = 'saeed'
print(username == str(username) and not None and len(username) <= 5 and username != '')

# 5. Check if the user is either an admin or a moderator,
#  either they're not banned or they've verified their email

email = 'saeed@gmail.com'
status = 'Admin'
banned = True

print(status == 'Admin' or status == 'moderator' and not banned or email != '')