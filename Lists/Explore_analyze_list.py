# Explore & Analyze List
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)
print("Length of List:", len(my_list))
print("minimum value:", min(my_list))
print("maximum value:", max(my_list))
print("Sum of List:", sum(my_list))


print("all elements are True?:", all(my_list))
print("any element is True?:", any(my_list))

print("Sorted List:", sorted(my_list))
print("Reversed List:", list(reversed(my_list)))

print("Count of 20 in List:", my_list.count(20))
print("Index of 30 in List:", my_list.index(30))

print("Is 40 in List?:", 40 in my_list)
print("Is 60 in List?:", 60 in my_list)
print("Is 60 in List?:", 60 not in my_list)
list1 = [10, 20, 30]
list2 = [10, 20, 30]
print(list1 == list2)
print(list1 is list2)

list1 = list2
print(list1 is list2)