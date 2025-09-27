c = (10,20,10,30,50,40,60,90,70,40,100,80,65,100,95)
unique=[]
duplicate=[]
for i in c:
    if i in unique:
        duplicate.append(i)
    else:
        unique.append(i)
print("Unique elements are:",unique)
print("Duplicate elements are:",duplicate)