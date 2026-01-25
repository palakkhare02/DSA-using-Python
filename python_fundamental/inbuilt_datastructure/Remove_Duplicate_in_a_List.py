def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        # Check if the item is already in the unique_list
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
 
# # Example usage
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
# print(remove_duplicates([4, 5, 5, 4, 6, 7]))     # Output: [4, 5, 6, 7]
 
