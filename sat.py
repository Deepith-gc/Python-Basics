# ---------------Print smallest number in the list-------------------
#l = [90,18,12,5,27,16]
# # print(min(l))
# # l.sort()
# # print(l[0])
#
# num =l[0]
# for i in l:
#     if i < num:
#          num=i
# print('Smallest number in the list is:',num)
#
# num=l[0]
# for i in range(0,len(l)):
#     if l[i]<num:
#         num=l[i]
# print('Smallest number in the list is:',num)



# ------------- Area of Triangle by taking user inputs---------------
# def find_Area(b,h):
#     Area=(1/2)*b*h
#     print(Area)
# find_Area(10,5)
# b=float(input('Enter the base value of triangle:'))
# h=float(input('Enter the height value of triangle:'))
# Area = (1/2)*b*h
# print('Area of triangle is:',Area,'sq units')



# ----------------Print multiples of 4 from 19 to 88 in reverse order using list comprehension-----------
# for i in range(88,19,-1):
#     if i%4==0:
#         print(i)
# print([i for i in range(88,19,-1) if i%4==0])



# ------Convert case of letters in the list-----
# case = ['a','B','c','D','e','F','g','H','i']
# for c in case:
#         if 'A' <= c <= 'Z':
#             new = (ord(c) + 32)
#             print(chr(new))
#         elif 'a' <= c <= 'z':
#             new = (ord(c) - 32)
#             print(chr(new))



# # ---------Dictionary--------
# d={'fruit':'apple','game':'cricket','place':'hassan'}
# # print(d.keys())
# # print(d.values())
# for i in d:
#      print(i,d[i])
# for i,j in d.items():
#      print(i,':',j)
# for i in  d.items():
#      print(i)