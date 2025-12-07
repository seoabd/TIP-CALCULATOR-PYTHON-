print("Welcome to the tip calculator!")
bill = float(input("What was the totall bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

percentage = tip / 100
total_bill = bill * (1 + percentage)
bill_split = total_bill / people

print(f"Each person should pay: {bill_split: .2f}")