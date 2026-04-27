"""print("******** Len*******")
l=[10,20,30,40]
print(len(l))
print(l)

l=[1,20,30,40,50,True,60,1]
print(l.count(1))

l=[20,30,1,True]
print(l.index(1))""

l=[10,20,30,True,10.2]
print(l)
l.append(40)
l.append('python')
l.append(50)
print(l)
l.append([60,70,80,90,])
print(l)

l=[20,30,1,True]
l.extend([40,50,60,70])
print(l)""

l=[20,30,1,True]
l.insert(1,40)
print(l)"

l=[20,30,1,True]
print(l)
l.remove()
print(l)
l= [1,2,3,4,5,7,6,9,10]
miss_number=set(range(l[0],l[-1]+1)) - set(l)
print(miss_number)"
l=[10,11.20,15,30,40,5]
l.sort()
print(l)
l.reverse()
print(l)"

l1=[10,20,30,40]
l2=[50,60,70]
l3=[True,'python',10.4]
ns=[l1,l2,l3]
print(ns)"

l=int(input("Enter a list elements:"))
print(max(l))
print(min(l))"

n=int(input("Enter a number:"))
if n>=1 and n<=100:
    print("between number is ",n)
else:
    print("The given number not between 1 and 100")

l1=[10,20,30]
print(l1*3)
l2=[40,50,60]
l3=[70,80,90]
l4=l1+l2+l3
print(l4)""
a,b,c,d=10,10.8,20,'puthon'
print([a,b,c,d])"
mylist=input("Enter a list of numbers separateed by space:")
mylist=list(map(int,mylist.split()))
sum=0
for num in mylist:
    print("The sum of the numbers is:",sum)

s=[x*x for x in range(1,11)]
print(s)
m=[x for x in s if x %2==0]
print(m)"""
a,b,c,d=10,20,10.5,'python'
print((a,b,c,d))


