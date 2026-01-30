def net_price(list_price,discount=0,tax=0.5):
    return list_price*(1-discount)*(1+tax)

print(f"The 1st Net amount is : {net_price(500)}")
print()

print(f"The 2nd Net amount is : {net_price(200,0.5)}")
print()

print(f"The 3rd Net amount is : {net_price(300,0.5,1)}")