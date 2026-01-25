def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    result = []
    for i in range(1, n + 1):
        result.append(str(i) * i)  # Repeat number i, i times
    return result

# Input
n = int(input("Enter the size of the number triangle: "))

# Generate triangle
triangle = generate_number_triangle(n)

# Print pattern
for row in triangle:
    print(row)