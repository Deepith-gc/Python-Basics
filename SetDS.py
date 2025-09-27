# s = {12,'dream','boy','girl','hat',90,30.45,8.6,True,False}
# print(s)
#
# s.copy()
# print(s)
# print('')
# s.remove(False)
# print(s)
#
# s.add('kite')
# print(s)
#
# s.clear()
# print(s)
#
# p={'red','blue','green','white','black'}
# s.update(p)
# print(p)

s=set()
for i in range(5):
    n=int(input(f"Enter number {i+1}:"))
    s.add(n)
print(s)
s.remove(int(input('Enter a value to remove:')))
print(s)
print(tuple(s).index((int(input('Enter a value to print position:')))))