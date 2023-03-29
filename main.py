pv = float(input("Enter the present value of the investment: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
years = int(input("Enter the number of years the investment will be held: "))

fv = pv * (1 + rate) ** years

print("The future value of the investment is:", round(fv, 2))


