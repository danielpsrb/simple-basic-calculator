num1 = float(input("Enter a First Number: "))
op = input("Enter operator: ")
num2 =float(input("Enter a Second Number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2) 
else:
    print("Invalid operator")