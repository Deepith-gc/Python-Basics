# 1
# str = input()
# print(str[len(str)-1:len(str)-4:-1])

# 2
# a=int(input('Enter the value of a:'))
# b=int(input('Enter the value of b:'))
# c=int(input('Enter the value of c:'))
# if a>b and a>c:
#     print(f"The largest is {a}")
# elif b>c:
#     print(f"The largest is {b}")
# else:
#     print(f"The largest is {c}")

# 3
# l = ['a',4,'hat',True,4.2,8.1,3.00,False,25,'can']
# print(l)
# l[1]='gcd'
# print(l)

# 4
# for i in range(80,59,-1):
#     print(i)
#print([i for i in range(80,59,-1)])

# 5
# d = {'name':'bharath','place':'Arsikere',0:28}
# '''
# for i in d:
#     print(i)
# for i in d.values():
#     print(i)
# for i in d.keys():
#     print(i)
# '''
# print(d)
# for i in d.items():
#     print(i)

# 6
# n = int(input("Enter a number: "))
# if n <= 1:
#     print("Enter a number greater than 1")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")

# 7
# str = input('Enter a word:')
# s1 = str[len(str)-1::-1]
# if str==s1:
#     print('Palindrome')
# else:
#     print('Not a palindrome')

# 8
"""
x = input("Enter a single character: ")

if len(x) != 1:
    print("Please enter only a single character.")
elif ('a' <= x <= 'z') or ('A' <= x <= 'Z'):
    # It's a letter
    if x in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Special character")

"""

# def check_character(ch):
#     if len(ch) != 1:
#         print("Please enter only a single character.")
#     elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
#         # It's a letter
#         if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
#             print("Vowel")
#         else:
#             print("Consonant")
#     else:
#         print("Special character")
#
# # --- Main Program ---
# x = input("Enter a single character: ")
# check_character(x)

# 9
def my_func(a, b, d=0, *c):
    print("a:", a)       # Positional
    print("b:", b)       # Positional
    print("d:", d)       # Default
    print("c (arbitrary):")
    for item in c:
        print(item)

my_func(10, 20, 30, 40, 50, 60)



# 10
# def show_items(*items):
#     print("Items passed to the function:")
#     for i, item in enumerate(items, start=1):
#         print(f"{i}. {item}")
#
# show_items("pen", "notebook", "eraser", "ruler")
