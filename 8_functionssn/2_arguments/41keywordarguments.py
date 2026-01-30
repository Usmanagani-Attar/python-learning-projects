def intro(greetings,tittle,first,last):
    print(f"{greetings} sir the {tittle} are from {first} to {last}")

intro("HELLO",last=10,tittle="numbers",first=1)

intro(greetings="HELLO",first=1,tittle="numbers",last=10)
print()



intro("Hi",last=20,first=2,tittle="even numbers")

intro("Hi","even numbers",2,20,)
print()




intro("HEY DEAR",last=30,first=3,tittle="3's multiples")

intro("HEY DEAR","3's multiples",first=3,last=30)
print()