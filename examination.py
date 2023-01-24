exam1=float(input('Enter the marks of exma 1(out of 100):'))
exam2=float(input('Enter the marks of exam 2(out of 100):'))
sport1=float(input('Enter the marks of sports exam(out of 50):'))
act1=float(input('Enter the marks of activity 1(out of 20):'))
act2=float(input('Enter the marks of activity 2(out of 20):'))
act3=float(input('Enter the marks of activity 3(out of 20):'))
exam=((exam1+exam2)*50)/200
sport=(sport1*20)/50
act=((act1+act2+act3)*30)/60
print('--------------RESULT-----------------')
print(f'The result of exam is : {exam}')
print(f'The result of activity is : {act}')
print(f'The result of sport is : {sport}')
print('--------------------------------------')
print(f'Total result : {(exam+sport+act)}')