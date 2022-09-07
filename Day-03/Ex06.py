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
 else:
  bill = 12
  print("Please pay $12")
 want_photo = input("Do you want a photo taken? Y or N. ")
 if want_photo == "Y":
  bill = bill + 3
 print(f"Your total bil is ${bill}") 
else:
 print('You cannot ride')

