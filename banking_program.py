def deposit(balance):
    amount=float(input("ENTER THE AMOUNT YOU WISH TO DEPOSIT : ₹"))
    balance+=amount
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"YOUR BALANCE IS {balance:0.2f}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    return balance

def withdraw(balance):
    amount=float(input("ENTER THE AMOUNT YOU WISH TO WITHDRAW : ₹"))
    if amount>balance:
        print("\n---------INSUFFICIENT BALANCE--------\n")
        return balance

    balance-=amount
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"YOUR BALANCE IS {balance:0.2f}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    return balance


def showbalance(balance):
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"YOUR BALNCE IS {balance:0.2f}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    return balance

balance=0
is_running=True

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
string1="BANKKING PROGRAM"
print(string1.center(36))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
while is_running:
    print("1. DEPOSIT MONEY")
    print("2. WITHDRAW MONEY")
    print("3. CHECK BALANCE")
    print("4. Exit")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    choice= int(input("ENTER YOUR CHOICE (1-4) : "))
    if(choice==1):
        balance=deposit(balance)
    elif(choice==2):
        balance=withdraw(balance)
    elif(choice==3):
        showbalance(balance)
    elif(choice==4):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("THANK YOU FOR CHOOSING OUR SERVICE")
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

        is_running=False
        break
    else:
        print("\n-----------INVALID INPUT------------\n")

