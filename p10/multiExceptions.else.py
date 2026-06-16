try :
    num = int( input("Enter a nummber:"))
    result = 10 /num
except ValueError:
    print("Error : Invalied input ! please enter a valied input number")
except ZeroDivisionError :
    print("Error : division by zero !")
else :
    print("Result :", result)
