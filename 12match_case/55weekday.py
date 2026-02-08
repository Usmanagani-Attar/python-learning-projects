def weekday(day):
    match day:
        case 1:
            return "It is sunday"
        case 2:
            return "It is monday"
        case 3:
            return "It is tuesday"
        case 4:
            return "It is wednesday"
        case 5:
            return "It is thursday"
        case 6:
            return "It is friday"
        case 7 :
            return "It is saturday"
        case _:
            return "Please enter valid day number"
    
        

print(weekday(1))
print()
print(weekday(2))
print()
print(weekday(3))
print()
print(weekday(4))
print()
print(weekday(5))
print()
print(weekday(6))
print()
print(weekday(7))
print()
print(weekday(9))

