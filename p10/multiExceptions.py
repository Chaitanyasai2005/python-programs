try:
    num = int( input("enter a number:"))
    result = 10/num
    print("Rsult:",result)
except ValueError :
    print("Erro :Invalied input ! please enter a valied number:")
except ZeroDivisionError :
    print(" Error : invaed division by zero error")
