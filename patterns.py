# # Two pointers
# s='maam'
# l,r=0,len(s)-1
# while l<r:
#     if s[l]!=s[r]:
#         print('Not a palindrome')
#         break
#         l=l+1
#         r=r-1
#     else:
#         print('Palindrome')
#         break

# # Math-Digit Loop
# n=456
# s=0
# while n>0:
#     s += n % 10
#     n //= 10
# print(s)

# # Hashing/Dict lookup
# l=[1,2,3,4,6]
# target=5
# seen={}
# for i,num in enumerate(l):
#     if target-num  in seen:
#         print('Pair is:',num,target-num)
#     seen[num] = i
# #Storing frequency
# s='banana'
# f={}
# for c in s:
#     f[c] = f.get(c,0)+1
# print(f)

#Array manipulation
# # Rearrange/ Move zeros to end
# a=[0,1,2,3,4,0,10,41,0]
# arranged= [x for x in a if x!=0] + [0]*a.count(0)
# print(arranged)

# l=[5,2,1,6,3,5,1,7,8,5,9,5]
# arr=[i for i in l if i!=5] + [5]*l.count(5)
# print(arr)

# Rotate array
p=[7,2,4,3,8,7,6,5,1,0,0,0,0]
k=4
k %= len(p)
rot = p[-k:] + p[:-k]
print(rot)