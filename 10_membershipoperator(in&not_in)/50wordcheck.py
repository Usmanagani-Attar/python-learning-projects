fruits={"apple","banana","pineapple","mango","orrange"}
a=input("Enter the fruit name to search : ")

if a in fruits:
    print(f"Your fruit {a} was found")
if a not in fruits:
    print(f"Your fruit {a} was  not found")