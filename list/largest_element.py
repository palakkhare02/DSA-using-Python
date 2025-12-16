def find_largest(numbers):
    largest = numbers[0]  # assume first element is largest
    
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    
    return largest
