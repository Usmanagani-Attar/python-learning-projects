#sum of 1st n numbers

a=int(input("Enter the limit of the element : "))
n=1
t=0
while(n<=a):
    print(n)
    t+=n
    n+=1
    
print(t)