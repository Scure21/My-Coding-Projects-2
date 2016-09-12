
def answer(heights):
    # Right off of the bat, water can't collect if there are fewer than 3 towers
    if len(heights) < 3:
        return 0
        
        
    primtowers = [(0, heights[0])]
    ultowers = [(len(heights) - 1, heights[-1])]
    
    for primcolumn in range(len(heights) - 1):
        if heights[primcolumn] >= primtowers[-1][1]:
            primtowers.append((primcolumn, heights[primcolumn]))
    print primtowers
    for ulcolumn in range(len(heights) - 1, 0, -1):
        if heights[ulcolumn] > ultowers[-1][1]:
            ultowers.append((ulcolumn, heights[ulcolumn]))
    print ultowers
    
    towers = sorted(list(set(primtowers) | set(ultowers)))
    print towers
    score = 0
    
    for column in range(len(towers) - 1):
        try:
            towerdiff = range(towers[column][0] + 1, towers[column + 1][0])
            waterlevel = min(towers[column][1], towers[column + 1][1])
        except IndexError:
                break
        for column in towerdiff:
            score += waterlevel - heights[column]
            print score
    return score