def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    result = []
    for i in range(1, n + 1):
        result.append('*' * i)
    return result

# Take input from user
n = int(input("Enter the size of the triangle: "))

# Generate triangle
triangle = generate_triangle(n)

# Print each row