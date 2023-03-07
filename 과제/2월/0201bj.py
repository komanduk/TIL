# 2525
# a, b = map(int, input().split())
# t = int(input())
# a = a+t // 60
# b = b+t % 60
# if b >= 60:
#     a += 1
#     b -= 60
# if a >= 24:
#     a -= 24
# print(a,b)

# 2798
# a, b = map(int, input().split())
# tmp = list(map(int, input().split()))
# result = 0
# for i in range(a):
#     for j in range(i+1, a):
#         for k in range(j+1, a):
#             if tmp[i]+tmp[j]+tmp[k] > b:
#                 pass
#             else:
#                 result = max(result, tmp[i]+tmp[j]+tmp[k])
# print(result)

# 9076
# T = int(input())
# for t in range(T):
#     scr = list(map(int, input().split()))
#     scr.remove(max(scr))
#     scr.remove(min(scr))
#     if max(scr) - min(scr) >= 4:
#         print('KIN')
#     else:
#         print(sum(scr))

#1526
# n = int(input())

# while True:
#     flag = True
#     for i in str(n):
#         if i != '4' and i != '7':
#             flag = False
#             n -= 1
#     if flag:
#         print(n)
#         break
