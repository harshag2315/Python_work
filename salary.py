basic=int(input('Enter the basic salary:'))
hra=(basic*10)/100
ta=(basic*5)/100
print(f'The salary of an employee is {basic-(hra+ta)}')
