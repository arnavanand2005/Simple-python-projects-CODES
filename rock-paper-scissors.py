import random

choices=["rock","paper","scissors"]
compscore=0
userscore=0
compchoice=random.choice(choices)

while True:
    compchoice=random.choice(choices)
    userchoice=input("ENTER YOUR CHOICE (scissors/paper/rock) (Enter q to quit): ")
    
    if userchoice=="q":
         print("-*-*-THANKS FOR PLAYING-*-*-\n")
         print(f"COMPUTER SCORE : {compscore} USERSCORE : {userscore}\n")
         if(userscore>compscore):
              print("\nCONGRATUALTIONS YOU WON!")
         elif(compscore==userscore):
            print("ITS A DRAW")
         else:
              print("COMPUTER WON")   
         break
    if userchoice not in choices:
           print("INVALID INPUT")
    else:
            print(f"YOU CHOSE {userchoice.capitalize()} AND COMPUTER CHOSE {compchoice.capitalize()}")
            userchoice=userchoice.lower()
            if userchoice.lower()==compchoice.lower():
                print("ITS A DRAW\n")
            elif (userchoice.lower()=="rock" and compchoice.lower()=="scissors") or (userchoice.lower()=="paper" and compchoice.lower()=="rock") or (userchoice.lower()=="scissors" and compchoice.lower()=="paper"):
                print("YOU WON!!!\n")
                userscore+=1
            else:
                print("YOU LOST\n")
                compscore+=1