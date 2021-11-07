principle = int(input("Enter principle amount: "))
monthly = int(input("Enter monthly deposit amount: "))
end_month = principle + monhtly
rate = int(input("Enter interest rate: "))
time = int(input("Enter time(years): "))

ci= principle * pow((1 + rate / 100), time) - principle

print("Compound interest is ",ci)