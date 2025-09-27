# list = ['a','B','c','D','e','F','g','H','i']
list = input("Enter a string:")
for c in list:
    if 'A'<= c <='Z':
        print(chr(ord(c)+32))

    elif 'a' <= c <= 'z':
        print(chr(ord(c) - 32))

"""
x = input('Enter a single character: ')

if len(x) != 1:
    print("Please enter only a single character.")
else:
    if 'a' <= x <= 'z':
        print('Lowercase')
    elif 'A' <= x <= 'Z':
        print('Uppercase')
    else:
        print('Special character')
"""

# def is_letter(char):
#     if len(char) != 1:
#         print("Enter a single character.")
#     elif 'a' <= char <= 'z':
#         print('Lowercase letter')
#     elif 'A' <= char <= 'Z':
#         print('Uppercase letter')
#     else:
#         print('Special character')
#
# x = input('Enter a single character: ')
# is_letter(x)


#
# x = input("Enter a single character: ")
#
# if len(x) != 1:
#     print("Please enter only a single character.")
# elif x.isalpha():
#     if x.lower() in 'aeiou':
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Special character")
