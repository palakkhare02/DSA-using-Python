def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers without using built-in functions.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    total_sum = 0
    current_even_number = 2
    
    # Loop through the first n even numbers and add them to total_sum
    for i in range(n):
        total_sum += current_even_number
        current_even_number += 2  # Increment by 2 to get the next even number
    
    return total_sum
