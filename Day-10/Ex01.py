def format_name(first_name, last_name):
 if first_name == "" or last_name == "":
  return "You did not provide valid inputs"
 f_name = first_name.title()
 l_name = last_name.title()
 return f"{f_name} {l_name}"

output = format_name("angela","ANGELA")
print(output)


