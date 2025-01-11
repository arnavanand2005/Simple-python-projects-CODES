unit=input("ENTER TEMPERATURE UNIT ( C --> FOR CELSIUS / F --> FOR FAHRENHEIT ) : ")
temp=float(input("ENTER TEMPERATURE VALUE : "))

unit=unit.upper()
if (unit=="C"):
    print("Converting into FAHRENHEIT...")
    fahrenheit=(temp *9/5) +32
    print(f"{temp}°C is {fahrenheit}°F")
elif (unit=="F"):
    print("Converting into CELSIUS...")
    celsius=(temp - 32) * (5/9)
    print(f"{temp}°F is {celsius}°C")
else:
    print("INVALID INPUT")

