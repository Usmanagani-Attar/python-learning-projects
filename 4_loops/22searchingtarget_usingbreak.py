#searching element in array
arr =[]
L=int(input("Enter the length of the element : "))
target=int(input("Enter the target element to search : "))
for i in range(1,L+1):
    arr.append(int(input(f"Enter the {i} element : ")))
print(arr)
for i in arr:
    if i==target:
        print(f"The element is found at index {arr.index(i)} ")
        break
    else :
        print(f"{i} is not equal to {target}")