from art import logo

print(logo)

#Calculator

def add(n1, n2):
 return n1 + n2

def subtract(n1, n2):
 return n1 - n2

def multiply(n1, n2):
 return n1 * n2

def divide(n1, n2):
 return n1/n2

operations = {
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide
}

end_calculation = False

while not end_calculation:
 num1 = int(input("What's the first number?: "))
 num2 = int(input("What's the second number?: "))


 operation_symbol = input("Pick an operation from the line above: ")

 calculation_function = operations[operation_symbol]
 answer = calculation_function(num1,num2)

 print(f"{num1} {operation_symbol} {num2} = {answer}")
 stop_calculation = input("Do you wanna stop the calculation? 'Y' or 'N'. ")
 if stop_calculation == 'Y':
  end_calculation = True


