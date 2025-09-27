l=[10,20,10,30,50,40,30,40,60,10,70,80]
d=set()
u=set()
for i in l:
    if i in u: #Since u is empty it exits the if block and element is 
    #added to unique when it appears first time
        d.add(i)
    else:
        u.add(i)
print(d)        
print(u)