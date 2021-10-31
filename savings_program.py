'''Program that calculates savings and interest'''

initial_savings = 5000
interest_rate = 0.03

print('Initial savings of ${}'.format(initial_savings))
print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(' Savings at beginning of year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')