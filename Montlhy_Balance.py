def account_balance(balance,annualInterestRate,monthlyPaymentRate):
    '''
    balance: Type int.
    annualInterestRate: Type float e.g: 0.2.
    monthlyInterestRate: Type float e.g: 0.04.
    '''
    #monthlyInterestRate = annualInterestRate / 12.0
    #minimumMonthlyPayment = montlhyPaymentRate*balance
    month = 1
    totalPaid=0
    
    while month <=12:
        #calculate the minimum monthly payment
        minimumMonthlyPayment = round(monthlyPaymentRate*balance,2)
        #calculate the unpaid balance of the month
        monthlyUnpaidBalance = round(balance - minimumMonthlyPayment,2)
        #calculate interest
        interest = round(monthlyUnpaidBalance * (annualInterestRate/12),2)
        #update the balance
        new_balance = round(monthlyUnpaidBalance + interest,2)
         
        #total paid 
        totalPaid = totalPaid + minimumMonthlyPayment
        
        
        print 'Month: ', month
        print 'Minimum monthly payment: ', minimumMonthlyPayment
        print 'Remaining balance: ', new_balance
        
        month+=1
        balance = new_balance
        
    print 'Total Paid: ', totalPaid
    print 'Remaining balance: ', new_balance
    return
        
        
       