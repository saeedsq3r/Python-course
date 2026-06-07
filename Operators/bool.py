print(True)
print(False)
print(type(True))
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))
print(bool(None))


email = "email#gmail.com"
phone = "123-456-7890"
username = "saeedsq3r"

# Allows registration
# if any field is filled
print(any([email, phone, username]))



# Allows registration
# only of all field is filled
print(all([email, phone, username]))



print(isinstance(True, bool))