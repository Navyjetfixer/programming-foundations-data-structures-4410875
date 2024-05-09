def find_second_smallest(my_list):
    if len(my_list) <= 1:
        return None
    else:
        smallest = float('inf')
        second_smallest = float('inf')
        
    for item in my_list:
        if item < smallest:
                second_smallest = smallest
                smallest = item
        elif item < second_smallest:
                second_smallest = item
    return second_smallest       

            
                

print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest([5]))
print(find_second_smallest([5, 3, 3, 2, 6]))