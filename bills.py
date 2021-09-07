# monthly bills with roommate
print('What month is it?:')
month = str(input())

print('How much is rent?:')
rent = float(int(input()))

print('How much is electric?:')
electric = float(int(input()))

print('How much is internet?:')
internet = float(int(input()))

final_bill = (float(int(rent) + int(electric) + int(internet)))

y = int(final_bill / 2)
print(month, "overall bills:", y)
