import csv

# Write CSV file
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write header row
    writer.writerow(["Name", "Age"])

    # Write data row
    writer.writerow(["Ali", 20])

# Read CSV file
with open("data.csv", "r") as f:
    reader = csv.reader(f)

    # Print each row
    for row in reader:
        print(row)

# DictWriter (write dictionary data)
with open("data2.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])

    # Write header
    writer.writeheader()

    # Write row
    writer.writerow({"name": "Ali", "age": 20})

# DictReader (read dictionary format)
with open("data2.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)

# Custom delimiter
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["A", "B"])

# Quote all values
csv.writer(open("data.csv","w"), quoting=csv.QUOTE_ALL)

# Skip header example
with open("data.csv") as f:
    next(f)

# Write multiple rows
writer = csv.writer(open("data.csv","w"))
writer.writerows([[1,2],[3,4]])

# List available CSV formats
print(csv.list_dialects())

# Register custom format
csv.register_dialect("mydialect", delimiter=",")

# Excel format
csv.excel

# Unix format
csv.unix_dialect