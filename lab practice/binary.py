"""a=1111
print(type(a))
print(a)
l=[10,20,30,40,'python',10,20,24]
print(l)
l[0]=100
print(l)

print("***** Operators*****")
a=10
b=20
print("The addition is:",a+b)
print("The subtraction is:",a-b)
print("The multiplication is:",a*b)
print("The division is:",a/b)
print("The modulor is:",a%b)


print("******Comparision Opertors*****")
a=10
b=20
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)


print("*****Logical Operator*****")
a,b,c,d=10,20,0,'python'
print(a or b)
print(c or d)


num=int(input("Enther the Student number:"))
name=input("Enter Student name:")
m1=int(input("Enter first subject markes:"))
m2=int(input("Enter second subject marks:"))
m3=int(input("Enter third subject markes:"))
print("Student num is:",num)
print("Student name is:",name)
print("Student m1 is:",m1)
print("Student m2 is:",m2)
print("Student m3 is:",m3)
               
a,b,c,d=24,10,15,20
print((a+d)*(c/d))
print(a+(b*c)/d)
print((a+b)*(c/d))
p=int(input("Enter the number:"))
if p %2==0:
    print("The given number is ERven")
else:
    print("The given number is Odd")


num=int(input("Enter the number:"))
if num % 2==0:
    print("The given number is even")
else:
    print("The given nuimber is odd")


year=int(input("Enter the year:"))
if year %4==0:
         print("The given year is Leap")
else:
    print("The given year is not leep")


num=int(input("Enter a number:"))
if num % 5==0:
    print(num)
else:
    print("The number is not divisible by 5")


num=int(input("Enter a number:"))
if num >= 0:
    print("The given number is positive")
else:
    print("The given number is Negative")

name=input("Enter your name:")
if name=="chaithu" or "chandhu" or "p":
    print("You are authoraizedf")
else:
    print("You are not authoraized")


n1=int(input("Enter the firist numbrer:"))
n2=int(input("Enter the second number:"))
if n1>=n2:
    print("The givin number is bigger")
else:
    print("The given number is not bigger")


n=int(input("Enter  aanumbe :"))
if n>=1 and n<=100:
      print("The given number is between 1 and 100")
else:
    print("The given number is not between in 1 and 100")"""


num1=int(input("Enter a number:"))
num2=int(input("Enter swecond number:"))
num3=int(input("Enbter the thord number:"))
if num1>num2 and num1>num3:
    print("The given number is biggest of all 3 numbers")
elif num2>num3:
    print("Th given number is biggest of all3 numbers")
else num1<num2 and num2<num3:
    print("All big")
