temp=float(input("Enter the temperature:"))
units=input("Is this temperature in Celsius or Fahrenheit (C/F):").upper()
if units=='C':
    temp=round((9*temp)/5+32,2)
    print(f"The temperature in Fahrenheit is {temp}F")
elif units=='F':
    temp=round((temp-32)*5/9,2)
    print(f"The temperature in Celsius is {temp}C")
else:
    print(f"{units} is invalid units of measurement!!")