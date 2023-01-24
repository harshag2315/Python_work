a=input('Enter the Name:')
b=int(input('Enter the SAP ID:'))
c=input('Enter the Roll Number:')
d=input('Enter the Course you choose:')
e=input('In which semester you are:')
num1=int(input('Enter the Number of PDS:'))
num2=int(input('Enter the number of Python:'))
num3=int(input('Enter the number of Chemistry:'))
num4=int(input('Enter the number of English:'))
num5=int(input('Enter the number of Physics:'))
perc=(num1+num2+num3+num4+num5)/5
cgpa=perc/10
print('Name:', a,'\nRoll Number:', c,'\t\tSAP ID:',b,'\nSemester:',e,end='')
print('\t\t\tCourse:',d)
print('Subject name: \tMarks')
print('PDS:\t\t', num1,'\nPyhton:\t\t', num2,'\nChemistry:\t', num3)
print('English:\t', num4,'\nPhysics:\t', num5)
print('Percentage:\t', perc,'%')
print('CGPA:', cgpa)
if cgpa==10 and cgpa>=9.1:
    print('Grade:O')
elif cgpa<=9 and cgpa>=8.1:
    print('Grade:A+')
elif cgpa<=8 and cgpa>=7.1:
    print('Grade:A')
elif cgpa<=7 and cgpa>=6.1:
    print('Grade:B+')
elif cgpa<=6 and cgpa>=5.1:
    print('Grade:B')
elif cgpa<=5 and cgpa>=3.5:
    print('Grade:C+')
else:
    print('Grade:F')
