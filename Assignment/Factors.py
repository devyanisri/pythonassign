a=int(input('enter the no.'))
i=1
count=0
sum=0
while i<=a:
    if (a%i)==0:
        count=count+1
        sum=sum+i
        print(i)
    i=i+1
print(count)
print(sum)