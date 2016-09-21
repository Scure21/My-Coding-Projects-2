#Code exercise from Interview Cake
#  words = [
#    'ptolemaic',
#    'retrograde',
#    'supplant',
#    'undulate',
#    'xenoepist',
#    'asymptote', # <-- rotates here!
#    'babka',
#    'banoffee',
#    'engender',
#    'karpatka',
#    'othellolagkage',
#]

#given a list of lexicographically ordered words find the one that made the list rotate

def find_rotation_point(words):
    '''
    Input: list of lexicographically ordered words with a rotation word
    Output: 
    '''

    first_word = words[0]

    Low = 0
    High = len(words) - 1

    while Low < High:

        # guess a point halfway between floor and ceiling
        Middle = Low + ((High - Low) / 2)

        # if guess comes after first word
        if words[Middle] > first_word:
            # go right
            Low = Middle
        else:
            # go left
            High = Middle

        # if floor and ceiling have converged
        if Low + 1 == High:

            # between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return High, Low
            
            
