# 10817
# N = list(map(int, input().split()))
# N.sort()
# print(N[1])

# 20001
# ori_tmp = []
# while True:
#     ori = input()
#     if ori == '문제':
#         ori_tmp.append(ori)
#     elif ori == '고무오리':
#         if ori_tmp:
#             ori_tmp.pop()
#         else:
#             ori_tmp.append('문제')
#             ori_tmp.append('문제')
#     elif ori == '고무오리 디버깅 끝':
#         break
# if ori_tmp.count('문제') > 0:
#     print('힝구')
# else:
#     print('고무오리야 사랑해')

# 1269
# a, b = map(int, input().split())
# Number1 = list(map(int, input().split()))
# Number2 = list(map(int, input().split()))
# Number1_tmp = set(Number1)
# Number2_tmp = set(Number2)
# tmp = Number1_tmp - Number2_tmp
# tmp2 = Number2_tmp - Number1_tmp
# print(len(tmp)+len(tmp2))

# 3052
# a = []
# for n in range(10):
#     tmp =int(input())
#     N_tmp = tmp%42
#     a.append(N_tmp)
# print(len(set(a)))

# 1181
# import sys

# N = int(input())
# tmp = []
# for n in range(N):
#     tmp.append(sys.stdin.readline().strip())
# tmpset = set(tmp)
# tmp = list(tmpset)
# tmp.sort()
# tmp.sort(key= len)
# print(tmp)
# for i in tmp:
#     print(i)