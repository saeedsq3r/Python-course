# while condition:

# Build counter from 1 to 5
# i = 1
# while i <= 5:
#     print("Iteration:", i)
#     i += 1


# Write a program that keeps asking "Do you agree?" until the user types "yes"
# answer = ''
# while answer != 'yes':
#     answer = input("Do you agree: ")
# print("thank you")

# ============= OR ============

while True:
    answer = input("Do you agree: ")
    if answer == 'yes':
        break
print("thank you")

#  =========================== Challenge ==================
# 3 attempts
# Yees within three attempts -> "Glad we are on the same page"
# Otherwise "# strikes, You are Out!"

attempts = 0
while attempts < 3 :
    answer = input("Do you agree: ")
    if answer == 'yes':
        print("Glad we are on the same page")
        break
    attempts += 1
else:
    print("***, You are Out!")

