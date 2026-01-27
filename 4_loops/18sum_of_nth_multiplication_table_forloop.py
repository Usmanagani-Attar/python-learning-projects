
#sum of n's multiples till n*10

t=0

n=int(input("enter the value of n "))
a=n
for a in range(a,((n*10)+1),n):
    print(a)
    t+=a
   
print(t)