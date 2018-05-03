import Calculator2
first_number = int(input("Enter first number"))
operand = str(input("Enter operand"))
second_number = int(input("Enter second number"))

if operand == "+":
   print(first_number + second_number)

elif operand == "-":
    print(first_number - second_number)

elif operand == "*":
    print (first_number * second_number)

elif operand == "/":
    print (first_number / second_number)
else :
    print ("This is invaild operand")
