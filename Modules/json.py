import json

data = {"name": "Ali", "age": 20}

# Convert dict to JSON string
print(json.dumps(data))

# Pretty JSON format
print(json.dumps(data, indent=4))

# Sorted keys JSON
print(json.dumps(data, sort_keys=True))

# Compact JSON format
print(json.dumps(data, separators=(",", ":")))

# Convert JSON string back to dict
json_string = json.dumps(data)
print(json.loads(json_string))

# Write JSON to file
with open("data.json", "w") as f:
    json.dump(data, f)

# Read JSON from file
with open("data.json", "r") as f:
    print(json.load(f))

# Convert list to JSON
print(json.dumps([1,2,3]))

# Convert tuple to JSON
print(json.dumps(("a","b")))

# Boolean to JSON
print(json.dumps(True))

# None to JSON null
print(json.dumps(None))

# Parse JSON string
print(json.loads('{"x":10}'))

# Unicode support
print(json.dumps({"a":1}, ensure_ascii=False))

# JSON encoder object
print(json.JSONEncoder())

# JSON decoder object
print(json.JSONDecoder())

# Nested JSON
print(json.dumps({"nested":{"x":1}}))