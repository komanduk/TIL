# 10769
# N = input()
# smile = N.count(':-)')
# sad = N.count(':-(')
# if smile == 0 and sad == 0:
#     print('none')
# elif smile > sad:
#     print('happy')
# elif sad > smile:
#     print('sad')
# else:
#     print('unsure')

# 2455

# tmp = {}
# total = 0
# for i in range(1, 5):
#     out_, in_ = map(int, input().split())
#     total_ = in_ - out_
#     total += total_
#     tmp[i] = total
# print(max(tmp.values()))

# 2606
v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
    
