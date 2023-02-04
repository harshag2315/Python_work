#Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#c) Count of all fruits from s1 and s2
s1=set()
s2=set()
n=int(input('Number of fruits you want to enter:'))
for i in range(0, n):
    s1.add(input('Enter the fruit:'))
m=int(input('Number of fruit you want to enter:'))
for j in range(0, m):
    s2.add(input('Enter the fruit:'))
s=s1|s2
sn=len(s)
print(f'The number of total fruits are {sn}')