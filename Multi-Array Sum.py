# Find the sum of all numbers in a multi-array array
# Example: Input:     arr=[1,[2,[3,4]],[5,6]]
#          Output:    21, the sum of 1+2+3+4+5+6


def  multi_array_sum( arr):
    '''
        Input: arr, array of arrays
        Output: int of the sum of all numbers in the multi-array
    '''
    suma = 0
    for m in xrange(len(arr)):
        if type(arr[m]) == list:
            suma += multi_array_sum(arr[m])
        else:
            suma += arr[m]
    return suma
    
            
        
            