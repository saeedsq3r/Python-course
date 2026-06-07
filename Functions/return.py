# Transformation functions

# def clean_name(name):
#     if not name:
#         return None
#     else:
#         cleaned = name.strip().lower()
#         return cleaned

def clean_name(name):
    lo_cleaned = name.strip().lower()
    up_cleaned = name.strip().upper()
    return lo_cleaned, up_cleaned


lo_name,up_name = clean_name("  SaeeD  ")

print(lo_name)
print(up_name)