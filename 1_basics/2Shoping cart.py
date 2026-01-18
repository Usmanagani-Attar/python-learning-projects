item = input('Enter the item name : ')
bug = float( input(f'Enter the budget of {item} : '))
quant = int(input(f'Enter the quantity of {item}s that u need : '))

total_price = (bug*quant)

print(f'The total price of your {item}s purchaed is {total_price}')