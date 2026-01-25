def insertion_sort(lst):
    n = len(lst)
    
    for current in range(1, n):
        current_card = lst[current]
        current_position = current - 1
        
        while current_position >= 0 and lst[current_position] > current_card:
            lst[current_position + 1] = lst[current_position]
            current_position -= 1
        
        lst[current_position + 1] = current_card
    
    return lst

"""
    Sorts a list of elements in ascending order using the Insertion Sort algorithm.

    Insertion Sort works by dividing the list into a sorted and an unsorted part.
    Each element from the unsorted part is picked and inserted into its correct
    position in the sorted part by shifting larger elements to the right.

    Time Complexity:
        Best Case: O(n)
        Average Case: O(n^2)
        Worst Case: O(n^2)

    Space Complexity:
        O(1) - In-place sorting

    Parameters:
        lst (list): A list of comparable elements to be sorted.

    Returns:
        list: The sorted list in ascending order.
 """

