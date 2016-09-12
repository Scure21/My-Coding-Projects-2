def reverse_string(string):
    '''
    O(n) time and space
    '''
    split = []
    string2 = ''
    for i in xrange(len(string)):
        split.insert(0,string[i])
        
    for i in range(len(split)):    
        string2 += split[i]
        
    return string2
    
    
def reverse_string2(string):
    '''
    O(n) time, O(1) space
    '''
    string_list = list(string)
    
    low = 0
    high = len(string)-1
    
    while low < high:
        string_list[low] , string_list[high] = string_list[high] , string_list[low]
        
        low +=1
        high -=1
        
        print low, high
        print string_list
        
    return ''.join(string_list)
    
    
def reverse_words(message):
    words_list = message.split(' ')
    
    low = 0
    high = len(words_list)-1
    
    while low < high:
        words_list[low] , words_list[high] = words_list[high] , words_list[low]
        
        low +=1
        high -=1
        
        print low, high
        print words_list
        
    return ' '.join(words_list)