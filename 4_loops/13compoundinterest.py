p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (as a percentage): "))
t = float(input("Enter time (in years): "))

amount = p * (pow((1 + r / 100), t))
ci = amount - p

print("Total amount after compounding:", amount)
print("Compound interest earned:", ci)
