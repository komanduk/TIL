# 9085
# T = int(input())
# sum_ = 0
# for t in range(1, T+1):
#     N = int(input())
#     Number = list(map(int, input().split()))
#     sum_ = 0
#     for n in Number: 
#         sum_ = n + sum_
#     print(sum_)

# 10824
# a,b,c,d = list(map(str, input().split()))
# result = a+b, c+d
# result2 = list(map(int, result))
# sum = 0
# for n in result2:
#     sum = n + sum
# print(sum)

#3009

# 10952
# while True:
#     a, b = map(int, input().split())
#     result = a+b
#     if result == 0:
#         break
#     else:
#         print(result)

# 1110
a = int(input())
x = a
C = 0
while True:
    A = x//10
    b = x%10
    c =(A + b)%10
    x = (b*10) + c
    C +=1
    if x == a:
        print(C)
        break
    


