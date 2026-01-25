def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation without using built-in functions.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    decimal_value = 0
    length = len(binary_str)
    
    # Iterate over each character in the binary string
    for i in range(length):
        # Get the digit (either '0' or '1')
        digit = binary_str[length - 1 - i]  # Start from the end of the string
        
        # If the digit is '1', add the corresponding power of 2 to the decimal value
        if digit == '1':
            decimal_value += 2 ** i  # Add 2 raised to the current power
 
    return decimal_value
