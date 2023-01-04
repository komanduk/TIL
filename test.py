n = int(input("정수"))
sum = 0
i = 0
#while n >= i:
#    sum += i
#    i += 1
#    print(sum)
for c in range(1, n+1):
    sum = c + sum
print(sum)
