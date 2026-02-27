# Find the index of an element in a list
def list_index(lst, element):
    """
    Returns the index of the first occurrence of element in lst.
    Raises ValueError if element is not found.
    """
    try:
        return lst.index(element)
    except ValueError:
        return -1

# Example usage
if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    
    # Find index
    index = list_index(numbers, 30)
    print(f"Index of 30: {index}")
    
    # Element not found
    index = list_index(numbers, 100)
    print(f"Index of 100: {index}")