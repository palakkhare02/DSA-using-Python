def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    result = []
    for i in range(1, n + 1):
        stars = '*' * (2 * i - 1)      # Number of stars in each row
        spaces = ' ' * (n - i)         # Spaces on each si*