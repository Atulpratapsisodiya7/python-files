a=int(input("Enter the njumbre"))
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1
    else:
        break
        
if c==2:
    print("yes")
else:
    print("not")
        
