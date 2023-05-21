# write a program to find  the sum of the digit of a given number.
i=int(input("enter the number="))
sum=0
while(i>0):
      sum=sum+i%10
      i=i//10
print("sum of the digit",sum)
