def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    result = []
    num = 1
    for i in range(1, n + 1):
        row_numbers = [str(num + j) for j in range(i)]
        result.append(' '.join(row_numbers))
        num += i
    return result

# Input
n = int(input("Enter the number of rows for Floyd's Triangle: "))

# Generate triangle
triangle = generate_floyds_triangle(n)

# Print patterns
for row in triangle:
    print(row)