def merge_dicts_with_overlapping_keys(dicts):
    # Initialize an empty dictionary to store the result
    result = {}
    
    # Loop through each dictionary in the list
    for d in dicts:
        # Loop through each key-value pair in the current dictionary
        for key, value in d.items():
            # If the key is already in the result dictionary, add the new value to the existing value
            if key in result:
                result[key] += value
            # Otherwise, add the key-value pair to the result dictionary
            else:
                result[key] = value
    
    return result
 
