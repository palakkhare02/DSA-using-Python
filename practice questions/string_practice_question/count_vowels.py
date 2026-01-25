def count_vowels(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Define the set of vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    # Initialize a counter for the vowels
    count = 0
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            count += 1  # Increment the count if it is a vowel
    
    # Return the total count of vowels
    return count
