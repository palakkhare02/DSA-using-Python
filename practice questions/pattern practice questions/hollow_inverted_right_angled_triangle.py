
def generate_hollow_inverted_right_angled_triangle(n):
    result = []

    for i in range(n, 0, -1):

        # First row → fully filled
        if i == n:
            result.append('*' * i)

        # Last two rows → always '*', '**'
        elif i <= 2:
            result.append('*' * i)

        # Middle hollow rows
        else:
            result.append('*' + ' ' * (i - 2) + '*')

    return result