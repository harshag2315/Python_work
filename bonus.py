#write a program to given bonus to their employ:
#if female and salary above 10000 give 10% bonus 
#if male and salary above 10000 give 5% bonus
##if female and salary below 10000 give 10% bonus and 2% extra bonus 
##if male and salary below 10000 give 5% bonus and 2% extra bonus 
salary=int(input('Enter the salary:'))
sex=input('Please enter the gender(M/m->male)(F/f->female):')
print('******************************************')
print(f'The original Salary={salary}')
if salary>=10000 :
    if sex=='M' or sex=='m':
        salary+=(salary*5)/100
    elif sex=='F' or sex=='f':
        salary+=(salary*10)/100
elif salary<10000:
    if sex=='M' or sex=='m':
        salary=salary+(salary*5)/100+(salary*2)/100
    elif sex=='F' or sex=='f':
        salary=salary+(salary*10)/100+(salary*2)/100
print(f'The total salary after the bonus:{salary}')
print('******************************************')
