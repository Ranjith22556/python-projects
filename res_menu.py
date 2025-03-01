menu={
    "biryani":200,
    "frypiece":100,
    "friedrice":150,
    "parata":50,
    "roti":40,
    "gobi":80,
    "kfc":300,
    "pepsi":30
}
cart=[]
total=0
print("------------MENU--------------")
for key,value in menu.items():
    print(f"{key:10} : $ {value}")
print("--------------------------------")
while True:
    food=input("Select the item(q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----------YOUR ORDER-------------")
for food in cart:
    print(f"{food:10} : {menu.get(food)}")
    total+=menu.get(food)
print("--------------------------------")
print(f"Your Total is {total}")
print("--------------------------------")