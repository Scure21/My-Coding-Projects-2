def array_diff(a, b):
    #your code here
    
    for x in a:
        for y in b:
            
            if y in a:
                a.remove(y)
            
    return a
    