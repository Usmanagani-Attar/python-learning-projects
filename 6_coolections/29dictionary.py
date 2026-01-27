capitals={"usa" : "washington","india" : "new delhi","china": "beijing","russia":"mosceow"}



print(capitals)
print()
print(capitals.get("usa"))
print()
capitals.update({"Germany":"Berlin"})

print()
print(capitals)


capitals.pop("china")
print(capitals)
print()

capitals.popitem()
print(capitals)
print()

print(capitals.keys())
print()

print(capitals.values())
print()

print(capitals.items())
print()

print(capitals.clear())