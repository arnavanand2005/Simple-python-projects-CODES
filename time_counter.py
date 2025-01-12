import time

timeinput=int(input("Enter NUMBER OF SECONDS TO SET A TIMER : "))

for i in range (timeinput,0,-1):
    hours=timeinput//3600
    timerem=timeinput%3600
    minutes=timerem//60
    seconds=timerem%60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    timeinput=timeinput-1

print("HAPPY NEW YEAR")

