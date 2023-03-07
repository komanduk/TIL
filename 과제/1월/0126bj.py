#10101
# tmp = []
# for n in range(3):
#     Number = int(input())
#     tmp.append(Number)
#     sum_ = sum(tmp)
#     print(sum_)
# for i in tmp:
#     if sum_ != 180:
#         print('Error')
#     elif tmp.count(60) == 3:
#         print('Equilateral')
#     elif len(set(tmp)) == 2:
#         print('Isosceles')
#     else:
#         print('Scalene')
#     break

# 2720
# T = int(input())
# for t in range(1, T+1):
#     money = int(input())
#     Quarter, tmp1 = money//25, money%25
#     Dime, tmp2 = tmp1//10, tmp1%10
#     Nickel, tmp3 = tmp2//5, tmp2%5
#     Penny = tmp3//1
#     print(Quarter, Dime, Nickel, Penny)

# 1453
# N = int(input())
# Number = list(map(int, input().split()))
# print(N - len(set(Number)))

# 10733

tmp = []
for n in range(int(input())):
    Number = int(input())
    if Number == 0:
        tmp.pop()
    else:
        tmp.append(Number)
print(sum(tmp))
