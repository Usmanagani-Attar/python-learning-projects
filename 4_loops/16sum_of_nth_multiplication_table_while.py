
#sum of n's multiples till n*10

t=0

n=int(input("enter the value of n "))
a=n
while(a<=(n*10)):
    print(a)
    t+=a
    a+=n
print(t)