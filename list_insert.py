# List insertion examples

# Create a sample list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# Insert at a specific index
fruits.insert(1, "orange")
print("After insert(1, 'orange'):", fruits)

# Insert at the beginning
fruits.insert(0, "mango")
print("After insert(0, 'mango'):", fruits)

# Insert at the end
fruits.insert(len(fruits), "grape")
print("After insert at end:", fruits)

# Using append (simpler for adding to end)
fruits.append("kiwi")
print("After append('kiwi'):", fruits)