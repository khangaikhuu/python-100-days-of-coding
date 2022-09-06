print('Welcome to the tip calculator')

total_bill = input('What was the total bill? \n')
percentage = input('What percentage tip would you like to give? 10, 12, or 15? \n')
people = input('How many people to split the bill?\n')

bill = (float(total_bill)/int(people)) * ((100 + int(percentage))/100)
print(f"Each person should pay: {round(bill,2)}")
