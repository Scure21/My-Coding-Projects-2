
def crop(string, start, length):
    """
    Returns a string with a specified index range removed
    """
    a = start
    b = start + length
    return string[:a] + string[b:]


def rclean(subject, search, difference):
    """
    Removes all occurrences of search starting at offset
    """
    index = subject.find(search, difference)

    length = len(search)

    while index != -1 and difference < length:
        subject = crop(subject, index, length)
        index = subject.find(search)

    return subject


def answer(chunk, word):
    """
    Returns the shortest, lexicographically earliest string that can be formed
    by removing occurrences of word from chunk.
    """
    results = []

    for difference in range(len(chunk) - len(word)):

        result = rclean(chunk, word, difference)

        if result != chunk:
            results.append(result)

    return sorted(results)[0]