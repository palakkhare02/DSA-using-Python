'''Problem Description

Sum of List Elements

Write a Python function that calculates the sum of all elements in a given list of integers.
'''

def sum_list(numbers):
    # Your code goes here
    total = 0
    for num in numbers:
        total += num
    return total