# class Sample:
#     x = 10  # Class variable
#
#     def __init__(self):
#         self.y = 20  # Instance variable
#
#     def instance_method(self):
#         print("Inside instance method:")
#         print("x =", Sample.x)
#         print("y =", self.y)
#
#     @classmethod
#     def class_method(cls):
#         print("Inside class method:")
#         print("x =", cls.x)
#         # Can't access self.y here because it's an instance variable
#
#     @staticmethod
#     def static_method():
#         print("Inside static method:")
#         print("x =", Sample.x)
#         # No access to self or cls, so y is not accessible
#
# # Create object
# obj = Sample()
#
# # a. Print x and y in all methods
# obj.instance_method()
# Sample.class_method()
# Sample.static_method()



# class A:
#     def instance_method(self, val):
#         print("Inside instance method. Value =", val)
#         self.value = val  # store to access later
#
#     @classmethod
#     def class_method(cls, param):
#         print("Inside class method. Param =", param)
#         cls.class_param = param  # store to access later
#
# # Create object
# a = A()
# a.instance_method(100)
# A.class_method(200)
#
# # Accessing the parameters outside
# print("Outside the class:")
# print("Instance param (value):", a.value)
# print("Class param:", A.class_param)


# class Demo:
#     x = 10  # class variable
#     y = 20  # class variable
#
#     @classmethod
#     def class_method(cls):
#         local_y = 20  # local variable
#         print("Inside class method:")
#         print("x =", cls.x)
#         print("local y =", local_y)
#
#     @staticmethod
#     def static_method():
#         local_y = 20
#         print("Inside static method:")
#         print("x =", Demo.x)
#         print("local y =", local_y)
#
# # a. print x and y values in both methods
# Demo.class_method()
# Demo.static_method()
#
# # b. Outside the class
# print("Outside the class:")
# print("x =", Demo.x)
# print("y =", Demo.y)

"""Index based operations with lambda """
# l=[10,13,12,14,15,17,16,18,19,20]
# # 10,12,15,16,19 --> find the even index element  using to filter ?
# m=list(filter(lambda x:l.index(x)%2==0,l))
# print(m)
# # 13,14,17,18,20 --> find the odd index element using to filter ?
# m=list(filter(lambda x:l.index(x)%2==1,l))
# print(m)
# # 10,12,16 --> find the even index even element using filter ?
# m=list(filter(lambda x:l.index(x)%2==0 and x%2==0,l))
# print(m)
# # 14,18,20 find the odd index even element  using to filter ?
# m=list(filter(lambda x:l.index(x)%2==1 and x%2==0,l))
# print(m)
# # 15,19 find the even index odd element using to filter ?
# m=list(filter(lambda x:l.index(x)%2==0 and x%2==1,l))
# print(m)
# # 13 17 find the odd index odd element using to filter ?
# m=list(filter(lambda x:l.index(x)%2==1 and x%2==1,l))
# print(m)



def cus_dec(fun):
        print('*-*-*-*-*-*-*-*-*-*-*-*')
        print('/+/+/+//+/+/+/+/+/+/+/+')
        fun()
        print("/-/-/-/--/-/-/-/-/-/-/-")
        print('|.|.|.|.|.|.|.|.|.|.|.|.|')
def greet():
    print('Welcome to Learning')
cus_dec(greet())