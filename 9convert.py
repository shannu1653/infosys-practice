# #Problem-Solving Example — Convert String Number
# n=input()
# print(int(n))
print(int("50"))
print(str(25))
print(float(10))
print(int(10.99))
print(isinstance(100,int))

# # 6. Take two numbers as input and print their sum.
# a,b=map(int,input().split())
# print(a+b)

# #7. Take a decimal number as input and print its integer part.
# a,b=map(float,input().split())
# print(int(a),int(b))

numbers=list(map(int,input().split()))
print(sum(numbers))
print(sum(numbers)//len(numbers))