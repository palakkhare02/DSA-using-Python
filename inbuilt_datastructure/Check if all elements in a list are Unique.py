def check_unique(lst):
    # Initialize an empty set to keep track of seen elements
    seen = set()
    
    # Iterate through each element in the input list
    for num in lst:
        # If the element has been seen before, return False
        if num in seen:
            return False
        # Add the element to the seen set
        seen.add(num)
    
    # If no duplicates are found, return True
    return True
 
