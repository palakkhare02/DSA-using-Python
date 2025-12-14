def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    result = []
    for i in range(n):
        result.append('*' * m)  # Append a row of '*' of length m
    
    return result

# Take input from user
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

# Generate rectangle
rectangle = generate_rectangle(n, m)

# Print each row
for row in rectangle:
    print(row)