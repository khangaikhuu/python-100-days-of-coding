def is_leap(year):
  """Take a first and last name and format it to return the title case version of the name. """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True 
      else:
        return False 
    else:
      return True 
  else:
    return False 
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month > 12 or month < 1:
   return "Invalid Input"
  days_in_month = month_days[month-1]
  isLeap = is_leap(year)
  if isLeap and month == 2:
   return days_in_month + 1
  return days_in_month 
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
