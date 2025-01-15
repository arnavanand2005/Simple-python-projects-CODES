stand ={"Salad" : 400,
        "Nuggets" : 450,
        "Popcorn (small)" : 420,
        "Popcorn (large)" : 600,
        "Nachos" : 510,
        "Burger" : 665,
        "Pizza" : 710,
        "Hot dog" : 385,
        "Juice" : 250,
        "Energy drink" : 330,
        "French fries" : 525
        }

order=[]
names=[]
prices=[]
final_price=0

print("\n-----------MENU-----------\n")
for key,value in stand.items():
    print(f"{key:20}: ₹{value:0.1f}")

for key,value in stand.items():
     key=key.lower()
     names.append(key) 
     prices.append(value)

print()
wont_order=True
while wont_order==True:
        choice=input("Enter what do you want to order : (Enter q to quit) : ")
        if choice.lower()=='q':
            wont_order=False
            print()
            print("*-*-*-*-*-*-*THANKS FOR VISITING*-*-*-*-*-*-*")
        elif choice.lower() not in names:
             print(f"Sorry {choice.capitalize()} is not availble with us at the moment")
             print()
        else:
             print(f"{choice.capitalize()}... added to your order")
             print()
             choice=choice.lower()
             order.append(choice)

print("\n---YOUR ORDER---")
for choice in order:
     fprice=stand.get(choice.capitalize())
     print(f"{choice.capitalize():20} : ₹{fprice:0.1f}")
     final_price+=fprice

print(f"THE TOTAL OF YOUR ORDER WILL BE : ₹{final_price:0.1f}\n")
