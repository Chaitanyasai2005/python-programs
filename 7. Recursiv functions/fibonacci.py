def fibonacci(Number):
    if(Number==0):
        return 0
    elif Number==1:
        return 1
    else :
        return fibonacci (Number-2)+ fibonacci(Number-1)
Number=int(input("please enter the fibonacci Number range="))
sum = 0
for num in range(Number):
    print(fibonacci(num),end='')
    sum = sum + fibonacci(num)
print("\n The sum of fibonacci series Numbers=%d%",sum)
