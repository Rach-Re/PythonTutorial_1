n= int(input())
sum=0
for i in range(n):
    x=int(input())
    sum=sum+x
avg=sum/n
print("The average is: {:.2f}".format(avg))
