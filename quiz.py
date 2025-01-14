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
questionno=0
score=0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[questionno]:
        print(option)

    guess=input("ENTER YOUR GUESS (A/B/C/D) : ")
    while guess.upper() not in ["A","B","C","D"]:
        print("INVALID CHOICE SELECTED ")
        print()
        guess=input("ENTER YOUR GUESS (A/B/C/D) : ")
    guess=guess.upper()
    guesses.append(guess)
    if guess==answers[questionno]:
        print("CORRECT ANSWER GUESSED ")
        score+=1
    else:
        print("WRONG CHOICE SELECTED")
        print(f"THE CORRECT ANSWER TO THE QUESTION WAS {answers[questionno]}")
        
    questionno+=1
print()

print(f"YOU SCORED {score} out of {len(questions)}")
print("*-*-*-*----END OF QUIZ----*-*-*-*")