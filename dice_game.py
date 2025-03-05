import random
while True:
    game_choice=input("Do you want to roll the dice? (y/n) : ") 
    if game_choice.lower()=="y":
        value1=random.randint(1,6)
        value2=random.randint(1,6)
        print(f"( {value1} , {value2} )")
    elif game_choice.lower()=="n":
        print("Thank you for playing the game!")
        break
    else:
        print("INVALID INPUT")