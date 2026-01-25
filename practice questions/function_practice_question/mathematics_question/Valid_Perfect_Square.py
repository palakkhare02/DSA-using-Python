def is_perfect_square(num):
    """
    Function to check if a number is a perfect square without using built-in functions.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False if num is not.
    """
    if num < 1:
        return False  # No perfect squares for numbers less than 1
    
    # Initialize a variable to keep track of the current number to check
    i = 1
    
    # Loop until i squared is greater than or equal to num
    while i * i <= num:
        if i * i == num:
            return True  # Found a perfect square
        i += 1  # Increment i to check the next integer
    
    return False
