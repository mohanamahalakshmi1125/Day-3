# list.pop() removes and returns an element from a list

# Create a sample list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Pop the last element (default)
last_fruit = fruits.pop()
print(f"Removed: {last_fruit}")
print(f"List now: {fruits}")

# Pop an element at a specific index
second_fruit = fruits.pop(1)
print(f"Removed at index 1: {second_fruit}")
print(f"List now: {fruits}")

# Pop from an empty list will raise an IndexError
# Uncomment to test: fruits.pop()