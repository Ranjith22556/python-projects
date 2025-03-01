weight=float(input("Enter the weight:"))
units=input("Enter units in 'L' or 'K':").upper()
if units=='K':
    weight=weight*2.205
    units='LBs'
    print(f"The weight in LBs is {round(weight,2)}{units}")
elif units=='L':
    weight=weight/2.205
    units='KGs'
    print(f"The weight in KGs is {round(weight,2)}{units}")
else:
    print(f"{units} is not a valid Unit!!")