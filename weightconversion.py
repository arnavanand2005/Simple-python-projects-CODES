weight=float(input("ENTER YOUR WEIGHT : "))
unit=input("ENTER THE UNIT YOU WISH TO  CONVERT INTO (l FOR pounds / Kg for kilograms) : ")
weightunit=unit.upper()

if(weightunit=="L"):
    converted=weight*2.205
    converted=round(converted,2)
    print(f"Weight {weight} Kg converted into pounds is {converted} Lbs")
elif(weightunit=="KG"):
    converted=weight/2.205
    converted=round(converted,2)
    print(f"Weight {weight} Lbs converted into KIlograms is {converted} Kg")
else:
    print("Invalid choice entered")
