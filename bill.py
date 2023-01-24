#write a program to calculate the bill:
qty=int(input('Enter number of items:'))
val=float(input('Enter the amount of given item:'))
dis=float(input('Enter the discount in percentage:'))
tax=float(input('Enter the tax:'))
amt=qty*val
discount=(amt*dis)/100
total_amt=amt-discount
total_tax=(total_amt*tax)/100
total_amount=total_amt+total_tax
print('************Bill**************')
print(f'Quantity sold : {qty}\nPrice per item: {val}')
print('------------------------')
print(f'Total amount: {amt}')
print(f'Total discount:{dis}')
print('-------------------------')
print(f'Total saving: {discount}')
print(f'Tax per item: {tax}')
print(f'Total tax: {total_tax}')
print('--------------------------')
print(f'Total amount to be paid: {total_amount}')