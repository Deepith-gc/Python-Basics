# d= {'fruit':'apple','animal':'dog','cricket':'sachin',1:10,4:400,3:40.0}
# print(d)
#
# print(d.items())
#
# # d.update()
#
# d.copy()
# print(d)
#
# d.pop(4)
# print(d)
#
# d.clear()
# print(d)

D={}
D['name']=input('Enter your name:')
D['city']=input('Enter your city:')
D['age']=int(input('Enter your age:'))
for i in D.items():
    print(i)

D['name']='gcb'
print(D)
del D['city']
print(D)

print(D.values())
c=input('Enter value to check:')
if c in D.values():
    print('Value exists in dictionary.')
else:
    print('Value does not exist in dictionary.')