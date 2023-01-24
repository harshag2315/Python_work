a=int(input('Enter the date (between 1 to 31): '))
b=int(input('Enter the month in numberic form (between 1 to 12): '))
c=int(input('Enter the year: '))
print('Date:', a,'Month:', b,'Year:', c)

if b==2:
    if c%400==0 or c%4==0 and c%100!=0:
        if  a!=29:
            print('Date:', a+1, 'Month:', b,'Year:', c)
        elif a==29:
            print('Date: 01 Month:', b+1,'Year:', c)
    else:
        if a==28:
            print('Date: 01 Month:', b+1, 'Year:', c)
        elif a!=28:
            print('Date:',a+1,'Month:', b, 'Year:', c)
elif b==1 or b==3 or b==5 or b==7 or b==8 or 10 or b==12:
    if a!=31 :
        print('Date:', (a+1), 'Month:', b, 'Year:', c)
    elif a==31 and b!=12:
        print('Date: 01 Month:', b+1, 'Year:', c)
    elif a==31 and b==12:
        print('Date: 01 Month: 01 Year:', c+1)
elif b==4 or b==6 or b==9 or b==11:
    if a!=30:
        print('Date:', (a+1), 'Month:', b, 'Year:', c)
    elif a==30:
        print('Date: 01 Month:', b+1, 'Year:', c)

