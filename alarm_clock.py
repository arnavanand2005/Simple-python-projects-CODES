import time
import datetime
import pygame

def set_alarm(alarmtime):
    print(f"ALARM SET UP FOR {alarmtime}")
    music_file="alarm_clock/alarmmusic.mp3"
    is_running=True

    while is_running:
            time_now=datetime.datetime.now().strftime("%H:%M:%S")
            print(time_now)
            if time_now==alarmtime:
                 print("WAKE UP!!! 🥲")
                 pygame.mixer.init()
                 pygame.mixer.music.load(music_file)
                 pygame.mixer.music.play()
                 while pygame.mixer.music.get_busy():
                      time.sleep(1)
                 break
            time.sleep(1)

                 
if __name__=='__main__':
    alarmtime=input("ENTER THE TIME TO SET AN ALARM FOR (HH:MM:SS) FORMAT : ")
    set_alarm(alarmtime)


