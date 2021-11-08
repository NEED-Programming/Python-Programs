# compounding interest calculator
# formula is
# A = P(1 + r/n)nt


principle = float(int(input()))
print('What is the', principle, ': ')

def compound_interest(principle, rate, time):

    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)

# Driver Code
compound_interest(10000, 10.25, 5)