#Welcome message
print("Welcome to the Tip Calculator.")

#Input the total bill
bill = float(input("What was the total bill?\n$"))

#Input the tip percentage
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15.\n"))

#Input the number of people
split = int(input("How many people to split the bill?\n"))

#Calculate the tip
tip = (bill * (tip_percentage / 100) )

#Calculate the total bill along with the tip.
total_bill = tip + bill

#Calculate the bill which has to be paid by each person.
result = round((total_bill/split), 2)

#Printing the result
print(f"Each person should pay ${result}.")
