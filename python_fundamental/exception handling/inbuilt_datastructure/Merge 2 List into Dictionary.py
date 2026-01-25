def merge_lists_to_dictionary(keys, values):
    # Boundary Condition to check for equal length of keys and values.
    # Last point in problem solving framework :)
    if(len(keys) != len(values)):
        return False
    # Create an empty dictionary to store the result
    result = {}
 
    # Use a loop to iterate through both lists
    for i in range(len(keys)):
        # Add each key-value pair to the dictionary
        result[keys[i]] = values[i]
 
    return result
 
