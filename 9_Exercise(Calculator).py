from webbrowser import Opera


first = input("Enter 1st number: ")
second = input("Enter 2nd number: ")
Operator=input("Choose operator +,-,*,/,% :")

first=int(first)
second=int(second)

if Operator == "+":
    print(first+second)
elif Operator == "-":
    print(first-second)
elif Operator == "*":
    print(first*second)
elif Operator == "%":
    print(first%second)
elif Operator == "/":
    print(first/second)
else:
    print("Thank you ")
