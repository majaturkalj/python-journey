print ("Welcome to the tip calculator")
totalBill = input("What was the total bill?\n")
totalBill_as_float = float(totalBill)

tip = input("What percentage tip would you like to give? 10, 12 or 15?\n")
tip_as_float = float(tip)
tip_as_percentage = float(tip_as_float/100)

splitPeople = input("How many people to split the bill?\n")
splitPeople_as_integer = int(splitPeople)
eachPersonPay = (totalBill_as_float + (totalBill_as_float * tip_as_percentage))/splitPeople_as_integer
eachPersonPayRound = round(eachPersonPay, 2)

print (f"Each person should pay: {eachPersonPayRound} $")