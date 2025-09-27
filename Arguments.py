#1
def find_sum(x, y, z):
    print("Sum of x y and z is:", x + y + z,'\n')
find_sum(10, 20, 30)

#2
def sum1(a,c,b):
    print("Sum of a b and c is:", a + b + c,'\n')
sum1(5, 15,b=10)

#3
def school(name, age, place):
    print("Name:", name)
    print("Age:", age)
    print("Place:", place,'\n')
school("Bharat", 27, place="Mysuru")

#4
def person(name, age, place="Bengaluru"):
    print("Name:", name)
    print("Age:", age)
    print("Place:", place,'\n')
person("Hari", 30, "Tumkur")
person("Dileep", 25)

#4
def student(name,*marks,clss=10):
    print("Name:", name)
    print("Marks:", marks)
    print("Class:", clss)
student('Kumar', 75, 80, 85, 90)