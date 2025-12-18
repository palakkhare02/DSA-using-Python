def count_even_odd(lst):
    # Initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Iterate through each number in the list
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            even_count += 1
        else:  # Otherwise, it's odd
            odd_count += 1
    
    # Return a tuple containing the counts of even and odd numbers
    return even_count, odd_count
 
