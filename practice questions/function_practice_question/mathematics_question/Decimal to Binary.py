def int_to_binary(n):
    """
    Function to convert an integer to its binary representation without using built-in functions.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    if n == 0:
        return "0"  # Special case for zero
 
    # Store the binary representation
    binary_representation = ""
    
    # Handle negative numbers
    is_negative = n < 0
    if is_negative:
        n = -n  # Work with the absolute value
 
    # Convert to binary
    while n > 0:
        remainder = n % 2
        binary_representation = str(remainder) + binary_representation  # Prepend the remainder
        n = n // 2  # Update n to be n divided by 2 (floor division)
 
    # Add the negative sign for negative numbers
    if is_negative:
        binary_representation = "-" + binary_representation
 
    return binary_representation
