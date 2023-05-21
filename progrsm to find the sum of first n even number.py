#write  a progrsm to find the sum of first n even number.
n=int(input("enter the number"))
i=1
sum=0
count=0
while(count<n):
 if (i%2==0):
                 sum=sum+i
                 count=count+1
                 i=i+1
print("sum of even number=",sum) 
