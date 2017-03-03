//Using Python
def get_permutations(string):

    # base case
    if len(string) <= 1:
        return set(string)
    
    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)
    
    # put the last char in all possible positions for each of the above permutations
    permutations_set = set()
        
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(string)):
            permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            permutations_set.add(permutation)

    return permutations_set
