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

#5.input().split() With Different Separators
arr=input().split(",")
print(arr[1])

#

