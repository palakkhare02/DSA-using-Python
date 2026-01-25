def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch.isalpha() and ch not in vowels:
            count += 1

    return count
