def int2str(i):
    digits = '0123456789'
    if i == 0:
        return 0
    result = ''
    while i > 0:
        result = digits[i%10] + result
        print result
        i = i/10
    return result
    
    
def digist2list(num):
    #num = str(num)
    l = []
    for i in num:
        l.append(int(i))
    return l