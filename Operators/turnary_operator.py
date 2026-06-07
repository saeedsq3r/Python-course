score = 50
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("F")

# inline method
grad = 'A' if score >= 90 else 'B' if score >= 80 else 'F'
print(grad)
# special Statement match case
# Convert the full coutry names into 2-letter abbreviations

country = "United States"
match country:
    case "United States" | "USA":
        abbr = "US"
    case "Canada":
        abbr = "CA"
    case "United Kingdom":
        abbr = "UK"
    case "Australia":
        abbr = "AU"
    case "Pakistan":
        abbr = "PK"
    case _:
        abbr = "Unknown Country"
print(abbr)