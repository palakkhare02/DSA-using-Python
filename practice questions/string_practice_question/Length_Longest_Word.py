def longest_word_length(s):
    """
    Function to find the length of the longest word in a string
    without using built-in string manipulation functions.
    """
    max_len = 0
    current_len = 0

    for ch in s:
        if ch != ' ':          # still inside a word
            current_len += 1
        else:                  # space found, word ended
            if current_len > max_len:
                max_len = current_len
            current_len = 0    # reset for next word

    # Check last word (if string doesn't end with space)
    if current_len > max_len:
        max_len = current_len

    return max_len
