def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    result = []
    for i in range(n):
        if i == 0 or i == n - 1:       # First and last row
            result.append('*' * n)
        else:                          # Middle rows
            result.append('*' + ' ' * (n - 2) + '*')
    return result

# Take input from user
n = int(input("Enter the size of the hollow square: "))

# Generate the hollow square
square = generate_hollow_square(n)

# Print each row of the hollow square
for row in square:
    print(row)