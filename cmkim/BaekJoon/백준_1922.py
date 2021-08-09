import heapq

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
# com = [[] for _ in range(n+1)]
# for _ in range(m):
#     s, e, c = map(int, input().split())
#     com[s].append([e, c])
#     com[e].append([s, c])

#com.sort(key=lambda x: x[2])
#com = sorted(com, key=lambda k: k[2])
#arr = sorted(arr, key=lambda k: k[2])
arr.sort(key=lambda x: x[2])
print(arr)