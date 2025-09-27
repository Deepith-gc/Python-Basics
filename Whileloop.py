# #Sum of a given digits
# # s=0
# # n=int(input('Enter a number:'))
# # while n!=0:
# #     r=n%10
# #     s=s+r
# #     n=n//10
# # print(s)
#
# #Palindrome
# # n=121
# # s=0
# # m=n
# # while n>0:
# #     r=n%10
# #     s=s*10+r
# #     n=n//10
# # if s==m:
# #     print('Number is a palindrome')
# # else:
# #     print('Number is not a palindrome')
#
# #Armstrong Number
# n=int(input('Enter a number:'))
# s=0
# m=n
# while n>0:
#     r = n % 10
#     s=s+r**(len(str(n)))
#     n=n//10
# if s==m:
#     print('Armstrong Number')
# else:
#     print('Not an Armstrong Number')

n=int(input('Enter a number to check if its prime:'))
i=2
if n<=2:
    print('Enter a value greater than 2')
while i<n:
    if n%i==0:
        print('Not a Prime number')
        break
        i=i+1
    else:
        print(' Prime number')
        break