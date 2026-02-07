num=(1,2,3,5,6,8,9)
a=int(input("Enter the number to search : "))
if a in num:
    print(f"Element {a} was found")
if a not in num:
    print(f"The number {a} was not found")