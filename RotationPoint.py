#Given a list of words in alphabetical order, find the word that caused the list to rotate
# for example: 
# words = [
#           'yogurt',
#           'xenon',
#           'zebra',
#           'zoo',
#           'burst',   <--This word causes the list to rotate
#           'course'
#         ]


def RotationPoint(words):
    '''
    Complexity: O(lg n) Time, O(1) Space
    '''
    First_word = words[0]
    Low = 0
    High = len(words) - 1
    print High
    while Low <= High:
        Middle = (High + Low) / 2
        if words[Middle] < First_word:
            High = Middle 
        else:
            Low = Middle 
        if Low +1 == High:
            return High

       
