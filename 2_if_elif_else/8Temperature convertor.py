''' Select the choice that is 
    select 1 for conversion of Celsius to Fahrenheit
     and 2 for conversion of Fahrenheit to Celsiuss

'''
choice = int(input('Select the choice 1 for C to F and 2 for F to C : '))

if(choice==1):
    C= float(input("Enter the value in Celsiuss : "))
    result = (C*(9/5))+32
    print(f'The value of {C}°C in Fahrenheit is {result}°F')
elif(choice==2):
    F= float(input("Enter the value in Fahrenheit : "))
    result = (F-32)*(5/9)
    print(f'The value of {F}°F in Celsius is {result}°C')
else:
    print('Please Enter only 1 or 2 ')