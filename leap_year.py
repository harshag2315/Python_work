#check whether the given year is leap year or not
year=int(input('Enter the year:'))
if year%4==0 and year%100!=0 or year%400==0:
    print('The year is leap year')
else:
    print('The year is not leap year')