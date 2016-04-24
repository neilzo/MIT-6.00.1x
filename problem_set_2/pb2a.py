# Paying the Minimum
# Passes with output in testCase_0.py
month = 1
balance = 4213
prevBal = balance
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentRate = 0.04
totalPaid = 0

while (month <= 12):
    minMonthPayment = round(prevBal * monthlyPaymentRate, 2)
    montlyUnpaidBal = round(prevBal - minMonthPayment, 2)
    prevBal = montlyUnpaidBal + (monthlyInterestRate * montlyUnpaidBal)
    totalPaid += minMonthPayment

    print 'Month: %d' % month
    print 'Minimum monthly payment: %5.2f' % minMonthPayment
    print 'Remaining balance: %5.2f' % prevBal
    if (month == 12):
        print 'Total paid: %5.2f' % totalPaid
        print 'Remaining balance: %5.2f' % prevBal
    month += 1
