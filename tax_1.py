#write a program to calculate the tax
#contdition-
#if income less than 150000 then no tax
#if income -->1,50,001-3,00,000 then 10% tax
#if income -->3,00,001-5,00,000 then 20% tax
#if income above than 5,00,001 then 30% tax
income=int(input('Enter the income:'))
print('****************************************************')
if income<=150000:
    print('No Tax')
    tax=-1
    print('****************************************************')
elif income>=150001 and income<=300000:
    tax=(income*10)/100
elif income>=300001 and income<=500000:
    tax=(income*20)/100
elif income>=500001:
    tax=(income*30)/100
if tax>=0:
    print(f'The tax is {tax}')
    print(f'The total income (after tax) is {income+tax}')
    print('****************************************************')