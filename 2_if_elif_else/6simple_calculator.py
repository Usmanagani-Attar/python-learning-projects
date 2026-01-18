operator = input("Enter an operator(+,-,*,/) : ")    

a = float(input('Enter the 1st element : '))
b = float(input('Enter the 2nd element : '))

if (operator=='+'):
    print(f'Sum of elements {a} and {b} is {a+b}')
elif (operator=='-'):
    print(f'Difference of elements {a} and {b} is {a-b}')
elif (operator=='*'):
    print(f'Product of elements {a} and {b} is {a*b}')
elif (operator=='/'):
    print(f'Division of elements that is  {a}/{b} is {a/b}')
else: 
    print("Please Enter the valid operator")