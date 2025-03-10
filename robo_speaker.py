import os

if __name__=="__main__":
    os.system("say Welcome to Robospeaker created by Arnav , I can speak anything you want me to speak")
    while True:
        command=input("ENTER WHAT DO YOU WANT ME TO SAY (Enter quit to exit the program): ")
        if command.lower()=="quit":
            os.system("say EXITING THE PROGRAM")
            print("THANK YOU FOR USING THE PROGRAM")
            break
        else:
            tospeak=f"say {command}"
            os.system(f"{tospeak}")