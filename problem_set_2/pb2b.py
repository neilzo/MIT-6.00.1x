# Paying Debt Off in a Year
balance = 4773
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
minMonthlyPayment = 10.0
cond = True

while cond:
    prevBal = balance
    for x in range(0, 12):
        monthlyUnpaidBal = prevBal - minMonthlyPayment
        prevBal = monthlyUnpaidBal + (monthlyInterestRate * monthlyUnpaidBal)
    if (prevBal <= 0):
        print 'Lowest Payment: %d' % minMonthlyPayment
        cond = False
    else:
        minMonthlyPayment += 10.0
