# membership operater in python

print("f" not in "hello")
print(5 in [1, 2, 3, 4, 5])
print("admin" in {"admin": "full access", "user": "limited access"})

# Security check: ensure the domain is not banned 
domain = "spam.net"
banned_domains = ["baddomain.com", "malicious.org", "spam.net"]
is_domain_allowed = domain not in banned_domains
print(is_domain_allowed)

# identity operaters
a = [1, 2, 3]
b = a
print(a is b)  # True, because b references the same object as a


c = [1, 2, 3]
d = [1, 2, 3]
print(c is d)  # False, because c and d are different objects with the same content

email = ""
print(email is not None and email != "")