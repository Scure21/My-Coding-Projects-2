def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    
    a = len(aStr)/2
    if aStr[a] == char:
        return True
        
        
    elif aStr[a] < char:
            return isIn(char,aStr[a+1:])
    return isIn(char, aStr[:a])
    
    