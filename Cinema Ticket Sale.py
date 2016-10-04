# It's not enough to only keep track of the amount of money collected
# we need to keep track of the amount of bills as well

def tickets(people):
    '''
        Input: array of ints with 25, 50 or 100 ordered dollars bill
        Output: string, YES if we can sell to all customers, NO is we can't
    '''
    # Dictionary to count the amount of each bill
    bills = {25:0, 50:0, 100:0}
    
    # update the values of the bills
    for dollar in people:
        if dollar == 25:
            bills[25] += 1
        elif dollar == 50:
            #if a customer comes with a 50 dollar bill and we don't have a 25, we can't sell a ticket
            if bills[25] == 0:
                return 'NO'
            # else, if we do have a 25 dollar bill, we can sel the ticket   
            bills[50] +=1
            bills[25] -= 1
        else:
            # for the 100 dollar bill:
            bills[100] += 1
            #we check first if we have both 50 and 25 bills to give the customer the change, so we can sell more
            if bills[50] >= 1 and bills[25] >= 1:
                bills[50] -= 1
                bills[25] -=1
            # If we don't have 50s and 25s, we check if we have 3 25 dollar bills to give the change
            elif bills[25] >= 3:
                bills[25] -= 3
            # if we don't have change for the 100 dollar bill, we return no
            else:
                return 'NO'
    # If we do have change a can sell all tickets, we return Yes
    return 'YES'
