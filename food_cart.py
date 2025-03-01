foods=[]
prices=[]
total=0
while True:
    food=input(("Enter the food item(Q to quit) : "))
    if food.upper()=="Q":
        break
    else:
        foods.append(food)
        price=float(input((f"Enter the price of {food} : $")))
        prices.append(price)
print("------YOUR CART-------")
for food in foods:
    print(food,end="    ")
for price in prices:
    total+=price
print()
print("The value of your cart is : $",total)