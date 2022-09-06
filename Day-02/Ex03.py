score = 0
height = 1.8
isWinning = True

# f-String
print(f"your score is {score} ")

age = input('What is your current age?\n')
death = (90 - int(age))
days = death * 365
weeks = death * 52
months = death * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left")
