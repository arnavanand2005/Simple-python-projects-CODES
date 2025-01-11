p=float(input("Enter principal amount : "))
while p<=0:
    print("PRINCIPLE AMOUNT CAN'T BE LESS THAN 0")
    p=float(input("Enter principal amount : "))

r=float(input("Enter rate of interest : "))
while r<=0:
    print(" RATE OF INTEREST CAN'T BE LESS THAN 0")
    r=float(input("Enter rate of interest : "))

t=int(input("Enter number of time periods elapsed : "))
while t<=0:
    print ("TIME PERRIODS ELAPSED CAN'T BELESS THAN 0")
    t=int(input("Enter number of time periods elapsed : "))

total=p*pow((1+r/100),t)
print(f"TOTAL BALANCE AFTER ${t} YEARS IS {total:.2f}")