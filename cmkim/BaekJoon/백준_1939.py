n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, b])

for i in range(1, n+1):
    print(arr[i])

start, end = map(int, input().split())


# 플로이드 워셜 반대로?
# for m in range(1, n+1):
#     for s in range(1, n+1):
#         for e in range(1, n+1):
#             if d[s][e] > d[s][m] + d[m][e]:
#                 d[s][e] = d[s][m] + d[m][e]


#print(d)
