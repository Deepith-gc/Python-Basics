# tup =(12,'pot',33.3,91,False,84,26,'pot')
# t=(90,30,70,24,56,48)
#
# print(tup.index(33.3))
#
# print(tup.index('pot',1,6))
# print(tup.count('pot'))

t = ()
z=list(t)
for i in range(5):
        n=int(input(f"Enter number {i+1}:"))
        z.append(n)
print(z)
z.remove(int(input('Enter a value to remove:')))
print(tuple(z))
print(tuple(z).index(int(input('Enter a value to print position:'))))