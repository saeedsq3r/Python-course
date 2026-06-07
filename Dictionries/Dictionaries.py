# Dictionary: Ordered, mutable, indexed using key
# no duplictaes for keys and allow for values

my_dict = {
    'a': 10,
    'b': 20,
    'c': 20,
    'a':40
}

print(my_dict)
# print(my_dict[1]) # Not Indexed
print(my_dict['b']) # using key
my_dict['c'] = 80

print(my_dict)

# Dict Methods
user = {"id":1, "age": 30, "city": "berlin"}

# Access
# print(user['name'])
print(user.get("name"))
print(user.get("age", "Unknown"))

# Checks
print("age" in user)
print("name" not in user)

# View Objects
print(user.keys())
print(user.values())
print(user.items())


# Looping

for u in user:
    print(u,user[u])

for key, value in user.items():
    print(key, value)


# Add, Remove, Update
user['name'] = "Saeed" # Add

user['age'] = 35 # Update

user.update({'age':40, "city":'paris'})

age = user.pop('age')
age = user.pop('salary',"Not Found")
user.popitem()
print(age)
print(user)


# Creation

user = {'id': None, "name": None, 'age': None, 'city': None}

user = dict.fromkeys(['id','name', 'age', 'city'], None)
print(user)

# =================== dict Challenge ====================
'''
1. Create New Dict
2. keep only paris with string Vlaues
3. Convert vlaues to Upercase
4. Elegan & Short solution!
'''
user = {
    'id': 1,
    'name': "saeed",
    'age': 30,
    'city': 'Berlin'
}

user_str = {
    k: v.upper()# Expression
    for k,v in user.items() # Loop
    if isinstance(v, str) # Filter
}
print(user_str)

# dict Real world applications

# Representing a Single Row from a Database or API
row = {
    'id': 1,
    'name': "saeed",
    'country': 'PK',
    'age': 30,
    'status': 'active'
}
# Mapping Translations to Frindly Values
status_map = {
    '01': "Open",
    '02': "In Progress",
    '03': "Done"
}

# Turning short abbreviations into full readable names.
country_map = {
    "DE": "Germany",
    "FR": "France",
    "IN": "India",
    "PK": "Pakistan"

}

# Storing Enviorment Variable & Configuration

system_conn = {
    "DB_HOST": "prod-db.company.com",
    "DB_PORT":54321,
    "DB_USER": "admin_user",
    'DB_NAME': "analytics_warehouse"
}

# Data About Data
table_metadata = {
    "table_name": "customers",
    "columns": {
        "id": {"type": "integer", "nullable": False},
        "name":{"type": "string", "nullable": True},
        "age": {"type": "integer", "nullable": True},
        "country": {"type": "string", "nullable": True}
    },
    "row_count": 105320,
    "file_format": "parquet",
    "last_update": "2024-10-01T12:45:00z",
    "partition_by": ['country'],
    "tags": ["pii", "customer-data"],
}
