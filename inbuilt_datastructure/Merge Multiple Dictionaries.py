def merge_three_dictionaries(dict1, dict2, dict3):
    # Create a new dictionary that starts with the content of dict1
    merged_dict = dict1.copy()
    
    # Add the key-value pairs from dict2
    for key, value in dict2.items():
        merged_dict[key] = value
    
    # Add the key-value pairs from dict3
    for key, value in dict3.items():
        merged_dict[key] = value
    
    return merged_dict
