def power(num):
    """
    Recursively computes and prints powers of 2 up to the given number.
    Returns the largest power of 2 less than or equal to num.
    """
    if num < 1:
        return 0
    elif num == 1:
        print(1)
        return 1
    else:
        prev = power(num // 2)
        curr = prev * 2
        print(curr)
        return curr
