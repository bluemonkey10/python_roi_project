import time

print("Enter your name below")
name = input("What are you waiting for?: ")
ss = input("Enter your social security number: ")
bankID = input("Enter your bank ID: ")
print("\n")

print(f"Hey, {name}! Welcome to the ROI calculator. \nYour Social Security Number is {ss} and your Bank ID is {bankID}. \nThanks for giving me that!")
print("\n")

valid = False
while not valid:
    try:
        totalIncome = float(input("To start, enter your average annual property income: "))
        totalExpenses = float(input("Now, enter your average annual property expenses \n(including property management, taxes, insurance, and maintenance): "))
        purchasePrice = float(input("Okay, just enter the property's purchase price: "))
        closingCosts = float(input("Almost there. Enter the property's closing costs: "))
        renovationCosts = float(input("Home stretch! Enter the property's renovation costs: "))
        valid = True
    except:
        print("Well, buds, looks like you done messed up. One more time!\n")

valid = False
while not valid:
    try:
        netProfit = float(totalIncome - totalExpenses)
        totalInvestment = float(purchasePrice + closingCosts + renovationCosts)
        basicROI = float((netProfit/totalInvestment) * 100)
        valid = True
    except:
        print("Gosh, we have to try this again. Dang it!")

print("\n")
print("Well, wasn't that fun?")
time.sleep(5)
print("What? Did you actually think I was going to give you your ROI for free? Ha!")
