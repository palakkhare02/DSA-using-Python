def generate_hollow_right_angled_triangle(n):
    result = []

    for i in range(1, n + 1):

        # First row → single star
        if i == 1:
            result.append("*")

        # Second row → always "**"
        elif i == 2:
            result.append("**")

        # Middle rows → star + spaces + star
        elif i < n:
            result.append("*" + " " * (i - 2) + "*")

        # Last row → fully filled
        else:
            result.append("*" * i)

    return result