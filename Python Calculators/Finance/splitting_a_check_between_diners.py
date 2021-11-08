# split your check between friends

def split_check(bill, people, tax_percentage = 0.09, tip_percentage = 0.15):
    tip = bill * tip_percentage
    tax = bill * tax_percentage
    total = bill + tip + tax
    return total / people
bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print('Cost per diner:', split_check(bill, people))

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))