def highestProductof3(array):
	'''
	Input: array containing at least 3 elements
	Ouput: Highest possible product of three elements of the array
	'''
	if len(array) < 3:
	    return 'There must be at least 3 elements!'

	highest = []
        for i in xrange(2):
	   max_elem = max(array)
	   highest.append(max_elem) 
	   array.remove(max_elem)
	   
	count = 0
	for num in array:
	    if num<0:
		count+=1
		
	if count >0:
	    lowest_elem = []
	    for i in xrange(2):
		min_elem = min(array)
		lowest_elem.append(min_elem)
		array.remove(min_elem)
	    return max(highest)*lowest_elem[0]*lowest_elem[1]
        else:
	    return max(array)*highest[0]*highest[1]
	    
	    
	    
	  
