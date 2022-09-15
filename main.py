
print("Welcome to the tip calculator!")
print("-------------------------------")

tBill = float(input("What was the total bill? $"))
tTip = float(input("How much to tip? %"))
tPeople = float(input("How many people to split the bill? "))

print("-------------------------------")

tTotalTip = tBill + (tBill * (tTip/100))
tSplitBill = tTotalTip / tPeople

print("Each person should pay: $" + "{:.2f}".format(tSplitBill))