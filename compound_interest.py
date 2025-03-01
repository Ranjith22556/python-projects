
while True:
    principle=float(input("Enter the principle:"))
    if principle<=0:
        print("Principle can't be negative or zero")
    else:
        break
while True:
    rate=float(input("Enter the rate:"))
    if rate<=0:
        print("rate can't be negative and zero")
    else:
        break
while True:
    time=float(input("Enter the time:"))
    if time<=0:
        print("time can't be negative and zero")
    else:
        break
total=principle*pow(1+rate/100,time)
print(total) 