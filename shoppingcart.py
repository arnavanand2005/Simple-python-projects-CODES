import time

foods=[]
prices=[]
total=0

while True:
    food=input("ENTER FOOD YOU WANT TO BUY (enter q to quit) [ NO SPACES ALLOWED!!! ] : ")
    if food=="q":
        print("THANKS FOR VISITING...!")
        break
    else:
        if not food.isalpha():
            print("INVALID INPUT ENTERED")
            time.sleep(1)
            print("PLEASE ENTER VALID INPUTS")
            time.sleep(1)
            print("")
        else:
            foods.append(food)
print()

for food in range(0,len(foods)):
    while True:
        try:
            price=float(input(f"ENTER PRICE FOR {foods[food]} : "))
            prices.append(price)
            break
        except ValueError:
            print("INVALID INPUT ENTERED")
print()

for price in prices:
    total+=price

print()

print("-----YOUR SHOPPING KART-----")
for food in foods:
    print(food)
print("___________TOTAL___________")
print(f"THE TOTAL OF YOUR BILL IS {total}")
print()