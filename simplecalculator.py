num1=float(input("ENTER THE FIRST NUMBER : "))
num2=float(input("ENTER THE SECOND NUMBER : "))

operation=input("CHOICE OF OPERATION YOU WANT ( + | - | * | / ) : ")

if  operation=="+":
    print(F"The sum of the numbers you provided {num1} & {num2} is {num2+num1}")

elif  operation=="-":
    print(F"The Difference of the numbers you provided {num1} & {num2} is {num1-num2}")

elif  operation=="*":
    print(F"The Product of the numbers you provided {num1} & {num2} is {num2*num1}")

elif operation=="/":
    if (num2==0):
        print("DIVISION BY 0 IS NOT POSSIBLE")
    else:
        print(F"The Quotient of the numbers you provided {num1} & {num2} is {num1/num2}")

else:
    print("OPERATION CHOICE INVALID")