def max_consecutive_difference(lst):
    # Edge case: if the list is empty or has only one element, return 0
    if len(lst) < 2:
        return 0
    
    max_diff = 0  # Initialize max difference as 0
    
    # Iterate through the list to calculate consecutive differences
    for i in range(1, len(lst)):
        current_diff = abs(lst[i] - lst[i - 1])  # Calculate absolute difference
        if current_diff > max_diff:  # Update max_diff if current_diff is greater
            max_diff = current_diff
    
    return max_diff  # Return the maximum difference
 
