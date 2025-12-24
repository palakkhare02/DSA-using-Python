def is_subset(lst1, lst2):
    # Iterate through each element of lst1
    for element in lst1:
        found = False  # Flag to check if element is found in lst2
        # Check each element of lst2
        for item in lst2:
            if item == element:  # Compare each element
                found = True
                break
        if not found:  # If any element from lst1 is not found in lst2, return False
            return False
    return True  # If all elements in lst1 are found, return True
