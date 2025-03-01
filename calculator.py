a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
operator=input("Enter the operator from the following [+,-,*,/,%]:")
if operator=="+":
    result=a+b
elif operator=="-":
    result=a-b
elif operator=="*":
    result=a*b
elif operator=="/":
    result=a/b
elif operator=="%":
    result=a%b
else:
    print("Invalid operator")
print("The result is:",result)

