# List extend example
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using extend() method to add all elements from list2 to list1
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# Extend with other iterables
list1.extend(['a', 'b', 'c'])
print(list1)  # Output: [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

# Extend with tuple
list1.extend((7, 8, 9))
print(list1)  # Output: [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 7, 8, 9]