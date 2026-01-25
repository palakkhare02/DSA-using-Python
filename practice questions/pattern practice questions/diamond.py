def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    result = []

    # Upper part (including middle row)
    for i in range(1, n + 1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        result.append(spaces + stars + spaces)

    # Lower part (mirror of upper part, excluding middle)
    for i in range(n - 1, 0, -1):
        stars = '*' * (2 * i - 1)
        spaces = ' ' * (n - i)
        result.append(spaces + stars + spaces)

    return result

# Input
n = int(input("Enter the number of rows for the diamond: "))

# Generate diamond
diamond = generate_diamond(n)

# Print result
for row in diamond:
    print(row)
