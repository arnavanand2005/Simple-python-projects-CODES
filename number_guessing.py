import random

randomnum=random.randint(1,100)
#print(randomnum) just for program checking

guessnum=0
print("\nPYTHON NUMBER GUESSING GAME")
while True:
    try:
        guess=int(input("ENTER A RANDOM NUMBER : "))
        if guess>100 or guess<0:
            print("NUMBER OUT OF RANGE!!! PLEASE CHOOSE BETWEEN (1-100) \n")
        else:
            if(guess>randomnum):
                print("YOUR GUESS IS TOO HIGH\n")
                guessnum+=1
            elif(guess<randomnum):
                print("YOUR GUESS IS TOO LOW\n")
                guessnum+=1
            else:   
                guessnum+=1 
                break
    except ValueError:
        print("INVALID INPUT GIVEN .. ONLY TO BE GIVEN IN AN (INT) DATA TYPE")
print(F"\nYOU GUESSED THE CORRECT NUMBER IN {guessnum} attempt(s)")
