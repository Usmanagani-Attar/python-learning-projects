#prints the numbers from 1 to n except 5's multiples
n=int(input("Enter the limit : "))

for i in range(1,n,2):
    if i%5==0:
        continue
    print(i)


#Actually prints 1 to 100 but stops at target element

target=int(input("Enter the target element : "))

for i in range(1,100):
    if i==target:
        print(i)
        break
    print(i)

