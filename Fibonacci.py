# Different solutions for Fibonacci with different time and space complexities

def fib(n):
    '''
    Time complexity O(2^n), space O(n), because of the stack
    '''
    
    assert type(n) == int,'element must be an int'
    if n < 0:
        return 'Number cant be negative'
    if n == 0 or n == 1:
        return 1
    else:
        #print n, 'fib(n-1): ', fib(n-1),'fib(n-2): ', fib(n-2)
        return fib(n-1)+fib(n-2)
        
#Fast Fib using memoization
#
def fastFib(x, memo):
    '''
    O(n), space and time for the first run, then it can grow 
    '''
    
    assert type(x) == int and x >= 0 and type(memo) == dict
    if x == 0 or x == 1:
        return 1
    if x in memo:
        return memo[x]
    result = fastFib(x-1, memo) + fastFib(x-2, memo)
    memo[x] = result
    #print memo
    return result
        

   
class Fibber:
    '''
     We can memoize to bring the cost of the time complexity to O(n)
     but it will take also O(n) for space since we are building up a call stack
    '''
    def __init__(self):
        self.memo = {}

    def fib(self, n):

        # edge case: negative index
        if n < 0:
            raise Exception("Index was negative. No such thing as a negative index in a series.")

        # base case: 0 or 1
        elif n in [0, 1]:
            return n

        # see if we've already calculated this
        if n in self.memo:
            return self.memo[n]

        result = self.fib(n-1) + self.fib(n-2)

        # memoize
        self.memo[n] = result

        return result
        
#We can build down the space to O(1) by a bottoms up approach

def fib_iterative(n):
    '''
    O(n) time and O(1) space.
    '''

    # edge cases:
    if n < 0:
        raise Exception("Index was negative. No such thing as a negative index in a series.")

    elif n in [0, 1]:
        return n

    # we'll be building the fibonacci series from the bottom up
    # so we'll need to track the previous 2 numbers at each step
    prev = 1
    prev_prev = 0

    # since we already initialized the first 2 numbers in the series
    # we take n - 2 steps ahead to reach n (xrange is exclusive)
    for _ in xrange(n - 1):
        current = prev + prev_prev
        print 'c: ',current
        prev_prev = prev
        print 'pp: ',prev_prev
        prev = current
        print 'p: ',prev

    return current
