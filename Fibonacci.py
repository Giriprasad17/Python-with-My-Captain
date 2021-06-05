#Fibonacci series
n = int(input("Enter the number of fibonacci series numbers to be printed:"))
#Print them using while loop
print("0,1,2",end=",")
a=1
b=2
#printing the rest of the series
while((n-3)>0):
    sum = a+b
    print(sum,end=",")
    a=b
    b=sum
    n=n-1
print(".....")
