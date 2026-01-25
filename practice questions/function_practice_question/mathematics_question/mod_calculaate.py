def mod(a, b):
    """Returns remainder of a divided by b, or -1 if b <= 0."""
    if b <= 0:
        return -1
    div = a // b
    return a - div * b

print(mod(5, 3))
