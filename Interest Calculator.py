import math

base = float(input('Enter initial savings: '))
print()

monthly = float(input('Enter monthly savings: '))
print()

rate = float(input('Enter annual interest % rate: '))
print()

years = int(input('Enter years that pass: '))
print()

total = base * math.pow(1 + (rate / 100), years)

print ('Savings after', years, 'years is', total)
