def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Initialize an empty string to hold the reversed version
    reversed_str = ''
    
    # Loop through the string in reverse order
    for i in range(len(s) - 1, -1, -1):
        # Concatenate each character to the reversed string
        reversed_str += s[i]
    
    # Return the reversed string
    return reversed_str