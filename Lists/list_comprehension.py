# list comprehension

domain = ['www.google.com', 'openai.com','localhost','www.saeed.COM']

cleaned = [
    # Data Transformation
    d.lower().replace('www.','')
    for d in domain
    if '.' in d
]


cleaned1 = [d for d in domain if '.' in d]


print(cleaned)



#         1.Transformation data   ,     2.Loop      ,   3.Filltring data
cleaned = [d.lower().replace('www.','') for d in domain if '.' in d]