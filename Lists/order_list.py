# Ordering of data in a list
my_list = [30, 10, 50, 20, 40]
print("Original List:", my_list)
# Sorting the list
sorted_list = sorted(my_list)
print("Sorted List:", sorted_list)
# Reversing the list
reversed_list = list(reversed(my_list))
print("Reversed List:", reversed_list)
# Sorting the list in place
my_list.sort()
print("List after in-place sort:", my_list)
# Reversing the list in place
my_list.reverse()
print("List after in-place reverse:", my_list)


my_list.sort(reverse=True)