import operator

def Merge(left, right, compare):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while (i < len(left)):
        result.append(left[i])
        i+=1
    while (j < len(right)):
        result.append(right[j])
        j+=1
    return result
    
def MergeSort(L, compare = operator.lt):
    if len(L) <2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = MergeSort(L[:middle], compare)
        right = MergeSort(L[middle:],compare)
        return Merge(left, right, compare)
    