def nfruits(fruitsList, pattern):
    '''
    function that receives a list of fruits with it's quantity and returns the maximum quantity in the List
    
    fruitsList: list with letters representing fruits and the quantity for each fruit
    pattern: a string containing a pattern of fruits consumed 
    
    '''
    
    assert len(fruitsList)<10, 'Too many fruits!'
    assert all(fruit >= 0 for fruit in fruitsList.itervalues()), "Pythin has no fruits of that kind!"
    assert fruitsList != {}, 'There are no fruits!'
    
    #Make sure pattern is in capitals
    pattern = pattern.upper()
    
    #Takes each character from pattern and saves it in a list
    newList = []
    for i in range(len(pattern)):
        newList.append(pattern[i])
        
        
    #Take the first letter in the pattern and consumes one from fruitsList
    while len(newList) > 1:
        i = 0
        if newList[i] in fruitsList:
            fruitsList[newList[i]] = fruitsList[newList[i]] - 1
    
    #Then buys 1 fruit of each type other than the one he just had
        for a in fruitsList.keys():     
            if a == newList[i]:
                fruitsList[a] = fruitsList[a]   
            else:
                fruitsList[a] = fruitsList[a] + 1
        newList = newList[i+1:]
        i+=1
        
    if len(newList) == 1:
        i = 0
        fruitsList[newList[i]] = fruitsList[newList[i]] - 1   
            
    return fruitsList[max(fruitsList, key=fruitsList.get)] 
        
        