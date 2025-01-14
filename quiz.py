questions=("What is the correct syntax for defining a function in Python?",
           "Which of the following is not a valid variable name in Python?",
           "Which method is used to add an element at the end of a list in Python?",
           "Which Python function is used to get the length of a list",
           "Which of these data types is immutable in Python?")
#You can add more questions according to you 

options=(["A) function = myFunction()","B) def myFunction():","C) function myFunction():","D) def function myFunction():"],
         ["A) _variable","B)2variable","C) variable2","D) variable_2"],
         ["A) add()","B) append()","C) insert()","D) push()"],
         ["A) len()","B) size()","C) count()","D) length()"],
         ["A) list","B) set","C) tuple","D) dictionary"])
#You can add more choices according to you 

answers=("B","B","B","A","C")
guesses=[]
score=0
initialques=0

for question in questions:
        print()
        print("----------------------------")
        print()
        print(question)
        for option in options[initialques]:
            print(option)
        
        guess=input("ENTER YOUR GUESS (A/B/C/D) : ")
        while guess.upper() not in ["A","B","C","D"]:
            print()
            print("INVALID INPUT ENTERED")
            guess=input("ENTER YOUR GUESS : ")
        
        guess=guess.upper()
        guesses.append(guess)

        if guess==answers[initialques]:
            print()
            print("CORRECT ANSWER")
            score+=1
        else:
            print()
            print("INCORRECT ANSWER!!!")
            print(F"CORRECT ANSWER WAS {answers[initialques]}")

        initialques+=1
print()
print("-----------------------RESULT-----------------------")
print(F"YOU SCORED {score} out of {len(answers)} MARKS")
print("THE ANSWERS TO THE QUESTIONS WERE : ")
for answer in answers:
    print(answer,end=" ")
print()
print("YOUR GUESSES WERE : ")
for guess in guesses:
    print(guess,end=" ")
print()
print("-*-*-*-*-*-*-*-THANKS-FOR-PLAYING-*-*-*-*-*-*-*-")
print() 
