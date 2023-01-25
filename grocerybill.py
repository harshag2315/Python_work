#write a program to calculate the bill of grocery
name=input('Enter the name of the grocery:')
qty=int(input('Enter the item quantity:'))
price=int(input('Enter the item price:'))
total_amt=qty*price
print('*******************BILL*********************')
print(f'Item Name\tItem Quantity\tItem Price\n{name}\t\t{qty}\t\t{price}')
print('********************************************')
print(f'Total Amount to be paid: {total_amt}')
print('********************************************')