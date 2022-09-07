print('Welcome to the rollercoaster!')
height = int(input("What is your height in cm? "))
bill = 0
if height>= 120:
 print('You can ride')
 age = int(input('What is your age?\n'))
 if age < 12:
  bill = 5
  print("Please pay $5")
 elif age <= 18:
  bill = 7
  print("Please pay $7")
 elif age >=45 and age <= 55:
  bill = 0
  print("Please do not pay")
 else:
  bill = 12
  print("Please pay $12")
 want_photo = input("Do you want a photo taken? Y or N. ")
 if want_photo == "Y":
  bill = bill + 3
 print(f"Your total bill is ${bill}") 
else:
 print('You cannot ride')

