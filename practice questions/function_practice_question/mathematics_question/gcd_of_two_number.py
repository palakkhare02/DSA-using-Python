def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Ensure n and m are positive
    n = abs(n)
    m = abs(m)
 
    # Use the Euclidean algorithm iteratively
    while m != 0:
        n, m = m, n % m  # Assign m to n and remainder of n divided by m to m
 
    return n  # When m becomes 0,n is the GCD

 
