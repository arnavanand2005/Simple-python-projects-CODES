import time
import datetime
import pygame

def set_alarm(alarm_time):
     alarm_sound="alarm_clock/alarmmusic.mp3"

     pygame.mixer.init()
     pygame.mixer.music.load(alarm_sound)

     while True:
          currenttime=datetime.datetime.now().strftime("%H:%M:%S")
          print(currenttime)

          if currenttime==alarm_time:
               print("TIME TO WAKE UP 🥲")
               pygame.mixer.init()
               pygame.mixer.music.load(alarm_sound)
               pygame.mixer.music.play()
               
               while pygame.mixer.music.get_busy():
                    time.sleep(1)
               break
          time.sleep(1)

if __name__=='__main__':
     in_loop="y"
     while in_loop=="y":
          try:
               hours=int(input("ENTER NUMBER OF HOURS YOU WANT TO SET AN ALARM FOR (24 hour format) : "))
               while True:
                    minutes=int(input("ENTER NUMBER OF MINUTES YOU WANT TO SET AN ALARM FOR : "))
                    if 0 <= minutes < 60: 
                         break
                    else:
                         print("MINUTES MUST BE BETWEEN 1-59")

               while True:    
                    seconds=int(input("ENTER NUMBER OF SECONDS YOU WANT TO SET AN ALARM FOR : ")) 
                    if 0 <= seconds < 60:
                         break
                    else:
                         print("SECONDS MUST BE BETWEEN 1-59")

               alarm_time=f"{hours:02}:{minutes:02}:{seconds:02}"
               print(f"ALARM SET FOR {alarm_time}")
               set_alarm(alarm_time)
               in_loop = input("Do you want to set another alarm? (y/n): ").lower() == "y"

          except ValueError:
               print("INVALID DATA TYPE ENTERED")
