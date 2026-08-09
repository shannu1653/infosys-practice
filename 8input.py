#INPUT() always returns a string
'''name=input()
print(name.split())


#1.Two Numbers on the Same Line
#suppose input is 10 20
a,b=map(int, input().split())
print(a,b)
list1=['23', '34', '45']
#@***map************
a=map(int,list1)
print(list(a))

#2.1Three Numbers
a,b,c=map(int,input().split())
print(a+b+c)

#2.2 Many Numbers ⭐⭐⭐⭐⭐ We don't know exactly how many variables we need.
numbers=list(map(int,input().split()))
print(numbers)

#3 Input With n
A common coding problem gives:

5
10 20 30 40 50

n=int(input())
arr=list(map(int,input().split()))
print(n)
print(arr)'''

# #4.Taking Multiple Strings
# language=input().split()
# print(language)

# #5.input().split() With Different Separators
# arr=input().split(",")
# print(arr[1])

#Practice set
# #1.Take an integer and print it.
# n=int(input())
# print(n)

# #2 Take two integers and print their sum.
# a,b=map(int,input().split())
# print(f"The sum of {a} and {b} is {a+b}")

# #3.Take two integers and print thier difference
# a,b=map(int,input().split())
# print(f"the difference between {a} and {b} is {abs(a-b)}")

# #4.Take two interger and print their product
# a,b=map(int,input().split())
# print(f"the product of {a} and {b} is {a*b}")

# #5.Take two integers and print thier division
# a,b=map(int,input().split())
# print(f"the division of {a} and {b} is {a//b}")

# ##LEVEL 2
# #6.Take 3 integers and print their average
# a,b,c=map(int,input().split())
# avg=(a+b+c)//3
# print(avg)

# #7.Take a number and print its square
# n=int(input())
# sqr=n*n
#sqr1=n**2
# print(sqr)

# #8.. Take a number and print its cube.
# n=int(input())
# print(n**3)

# #9.Take two numbers on the same line and print the larger number.
# a,b=map(int,input().split())
# if a>b:
#     print(f"{a} is larger than {b}")
# else:
#     print(f"{b} is larger than {a}")

# #10.Take five numbers on one line and print their sum.
# numbers=list(map(int,input().split()))
# sum1=0
# for num in numbers:
#     sum1+=num
# print(sum1)

##numbers = map(int, input().split())

'''Remember:
map → one-time use
list → reusable multiple times.'''
# print(sum(numbers))
# for i in numbers:
#     print(i)
# print(len(list(numbers)))

# print(max(2,3,4,5))

# # Level 3 ⭐
#11 n=int(input())
# arr=list(map(int,input().split())) #space O(n)
# print(sum(list(map(int,input().split()))))
# print(sum(arr))

# #12.print the largest number
# n=int(input())
# arr=list(map(int,input().split()))
# val=arr[0]
# for i in arr[1:]:
#     if i>val:
#         val=i
# print(val)
#max with amp
# print(max((map(int,input().split()))))

# #13.sum with map
# n=int(input())
# print(sum(map(int,input().split())))

# #14.Take a string and print its length.
# name=input().split(" ")
# print(len(name))
# print(len(input()))

#15.Take three integers and print then in reverse order
arr=list(map(int,input().split()))
rev=[]
for i in arr[::-1]:
    rev.append(i)
print(*rev)

print(*map(int, input().split())[::-1])
