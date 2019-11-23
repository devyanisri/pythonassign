#Fibonacci series
a=int(input("enter the number"))
f,s=0,1
for i in range(2,a):
    next=first+second
    print(next,end=" ")
    f,s=s,next
    