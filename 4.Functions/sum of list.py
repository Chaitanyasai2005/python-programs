def calculate_sum(numbers):
    total=0
    for num in numbers:
        total += num
    return total
numbers=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    num=int(input("Enter element{}:".format(i+1)))
    numbers.append(num)
result=calculate_sum(numbers)
print("The sum of the list is",result)
