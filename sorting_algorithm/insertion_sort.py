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
