def bubble_sort(lst):
    # Your code goes here
      
    n = len(lst)
    
    # Traverse through all list elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    
    return lst

