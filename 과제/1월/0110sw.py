T = int(input())
for t in range(1, T+1):
    n = list(map(int, input().split()))
    a =sum(n)/len(n)
    print(f'#{t} {round(a)}')

# T = int(input())
# for t in range(1, T+1):
#     a, b = list(map(int, input().split()))
#     tmp = a // b
#     tmp_ = a % b
#     print(f'#{t} {tmp} {tmp_}')

a, b = list(map(int, input().split()))
for i in [a+b, a-b, a*b, a//b]:
    print(i)

# n = int(input())
# tmp = ''
# for e in range(n):
#     tmp += '#'
# print(tmp)

# T = int(input())
# for t in range(1, T+1):
#     n = list(map(int, input().split()))
#     print(f'#{t} {max(n)}')