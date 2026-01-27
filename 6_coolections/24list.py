fruits = ["apple","mango","banana","banana","pineapple","orange","coconut"]

# print(dir(fruits))
# print()

# print(help(fruits))
# print()

print(len(fruits))
print()

print(fruits[3])
print()

print("apple" in fruits)
print("grapes" in fruits)
print()

fruits[0]="pineapple"
print(fruits)
print()
fruits[0]="pineapple"
print(fruits)
print()

fruits.append("grapes")
print(fruits)


fruits.remove("banana")
print()
print(fruits)

print()
fruits.insert(3,"apple")
print(fruits)

print()
fruits.sort()
print(fruits)

print()
fruits.reverse()
print(fruits)

print()
print(fruits.index("apple"))



print()
print(fruits.count("pineapple"))
print(fruits)

fruits.clear()
print(fruits)
