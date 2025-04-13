print("Welcome to the tipe calculator!")

total_amount = float(input("What was the total bill?"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15?"))
people_amount = int(input("How many people to split the bill?"))

amount_to_pay = ((total_amount * (tip_amount/(100+1))) + total_amount)/people_amount
net_amount = round(amount_to_pay,2)
print(f"Each person should pay: ${net_amount}")