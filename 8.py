# Take two sets and apply various set operations on them :
#    S1 = {Red ,yellow, orange , blue }
#    S2 = {violet, blue , purple}
s1 = {'Red' ,'yellow', 'orange' , 'blue' }
s2 = {'violet', 'blue' , 'purple'}
#add
s1.add('pink')
s2.add('pink')
print(f'{s1}\n{s2}')
#remove
s1.remove('pink')
s2.remove('pink')
print(f'{s1}\n{s2}')
#Union
s=s1|s2
print(s)
#intersection
s=s1&s2
print(s)
#difference
s=s1-s2
print(s)
s=s2-s1
print(s)
#symmetric difference
s=s1^s2
print(s)
