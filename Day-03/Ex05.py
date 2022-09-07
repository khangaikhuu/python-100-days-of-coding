# leap year

year = int(input('Give a year '))

if year % 4 == 0:
 if year % 100 == 0:
  if year % 400 == 0:
   print(f"The {year} is a leap year")
  else:
   print(f"The {year} is not a leap year")
 else:
  print(f"The {year} is a leap year")
else:
 print(f"The {year} is not a leap year")
