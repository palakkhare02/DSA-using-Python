def generate_number_pyramid(n):
    result = []

    for i in range(1, n + 1):
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        spaces = ' ' * (n - i)
        result.append(spaces + numbers)

    return result