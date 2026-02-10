#scope resolution in ppython has the rule of (LEGB) which is Local->Enclosed->Global->Built-in

#That means python intially checks for the local variable then will go for the enclosed variable then ...........

import math
print(math.e)
def func1():
    e=1
    print(e)

    def func3():
        print(e)

def func2():
    e=3
    print(e)

e=4
func1()
func2()


