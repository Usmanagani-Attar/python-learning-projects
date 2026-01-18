''' Select the choice that is 
    select 1 for conversion of Killogram to Pounds
     and 2 for conversion of Pounds to Killograms

'''
choice = int(input('Select the choice 1 for K to P and 2 for P to K : '))

if(choice==1):
    k= float(input("Enter the value in Killograms : "))
    result = k*2.205
    print(f'The value of {k} Killograms in Pounds is {result}')
elif(choice==2):
    p= float(input("Enter the value in Pounds : "))
    result = p/2.205
    print(f'The value of {p} Pounds in Killograms is {result}')
else:
    print('Please Enter only 1 or 2 ')