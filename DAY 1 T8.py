def is_valid_number(num):
    # Define the components of a valid number
    components = [4, 3, 2, 1]

    # Check if the number can be split into the components
    for component in components:
        if num >= component:
            num -= component
        else:
            return False

    # Return True if the number has been fully split
    return num == 0

# Test the function with some examples
print(is_valid_number(6)) # True
print(is_valid_number(9)) # False
