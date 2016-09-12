def duplicates2(array):
    
    n = len(array) -1
    loop_start = n+1
    # get inside a cycle
    for num in xrange(n):
        cycle = array[loop_start -1]
    #find leght of the cycle
    position_in_cycle = cycle
    current_cycle_position = array[cycle-1]
    step = 1
    
    while current_cycle_position != position_in_cycle:
        current_cycle_position = array[current_cycle_position-1]
        step += 1
    
    #Find the first node of the cycle
    pointer_start = n+1
    pointer_head = n+1
    
    for _ in xrange(step):
        pointer_head = array[pointer_head -1]
        
    while pointer_start != pointer_head:
        pointer_start = array[pointer_start - 1]
        pointer_head = array[pointer_head - 1]
        
    return pointer_start
    
    
    
def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # whoops--no duplicate
    raise Exception('no duplicate!')