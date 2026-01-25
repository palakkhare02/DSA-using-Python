def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    result = []
    for i in range(n):
        result.append('*' * (n - i))
    return result

# Take input from user
n = int(input("Enter the size of the inverted triangle: "))

# Generate inverted triangle
triangle = generate_inverted_triangle(n)

# Print the triangle
for row in triangle:
    print(row)