def  maxLength(a, k):
    '''
        Input: a, array with integers
               k, maximum value
        Output: maximum length of the largest subset which sum is k
    
    '''
    
    # a=[4,3,1,2,1], k=4
    # subsets = [[3],[1],[2],[1],[3,1],[1,2],[2,1],[1,2,1]]
    # output = 3, [1,2,1]
    
    subsets = []
    
    for i in xrange(len(a)):
        
        if a[i] < k:
            temp = [a[i]]
            Sum = a[i]
            tempSum = a[i]
            subsets.append([a[i]])
            
            for j in xrange(i,len(a)):
                if j != i:
                    Sum += a[j]
                    
                    if Sum < k:
                        temp.append(a[j])
                        subsets.append(temp)
                        tempSum = Sum
                        
                    elif Sum == k:
                        Sum = tempSum
                        temp.append(a[j])
                        subsets.append(temp)
                        temp = temp[:-1]
                    else:
                        Sum = tempSum
    lengths = []
    for subset_item in subsets:
        lengths.append(len(subset_item))
                
    return max(lengths) , subsets[lengths.index(max(lengths))] 
                
        
            
   

        
        
        
    
    