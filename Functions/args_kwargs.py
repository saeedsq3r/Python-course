# *args
# it is used when the type of data are same
# it is used when we want to pass a variable number of positional arguments to a function.
def total(*args):
    print(sum(args))

total(1,2,5,46,8,9,7)

# **kwargs
# it is used for multi data types 
# it is used when we want to pass a variable number of keyword arguments to a function.
def create_user(**kwargs):
    print(kwargs)

create_user(name='saeed',age=20,department='AI')