# Using Bisection Search to Make the Program Faster
balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0
minMonthlyLowerBound = balance / 12
minMonthlyUpperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
cond = True

while cond:
    prevBal = balance
    minMonthlyPayment = (minMonthlyLowerBound + minMonthlyUpperBound) / 2
    for x in range(0, 12):
        monthlyUnpaidBal = prevBal - minMonthlyPayment
        prevBal = monthlyUnpaidBal + (monthlyInterestRate * monthlyUnpaidBal)
    if (prevBal < -0.01):
        minMonthlyUpperBound = minMonthlyPayment
    elif (prevBal > 0.01):
        minMonthlyLowerBound = minMonthlyPayment
    else:
        print 'Lowest Monthly Payment is: %5.2f' % round(minMonthlyPayment, 2)
        cond = False
