print("Hello User" '\n')

list = [10,20,30,40.5,True,False]
print(list)
print(list + [50])
print(list)
list.append(30)
print(list)
list[5] = 9+0j
print(list[-3:])

print('\n')
tuple = (20,40,60,3.142,4+2j,'string')
print(tuple)
print('\n')

set = {30,60,90,100,"text",120,8.256,9j}
print(set)
set.add(150)
print(set)
#set[2] = 110 # Set elements are immutable

c = {'a':1,'b':2,'3':'Three','Four':'Pen'}
c['Book'] = 'Periwinkle'
print(c)
print(c['a'])
c['a'] = 10
print(c['a'])
print(c)