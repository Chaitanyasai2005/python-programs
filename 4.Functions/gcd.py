def gcd(a,b):
    while b!=0:
        a,b= b, a%b
    return a
num1 =int(input("Enter first numbers:"))
num2=int(input("enter the second nunber:"))
result=gcd(num1,num2)
print("The GCD of",num1,"and",num2,"is",result)
             
