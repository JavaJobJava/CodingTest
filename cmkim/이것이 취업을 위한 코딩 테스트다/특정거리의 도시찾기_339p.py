from _collections import deque

n, m, k, x = map(int, input().split())

arr = [[] for _ in range(n+1)]
dist = [1000000000] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    #arr[b].append(a)

q = deque()
q.append((x, 1))

while q:
    start, cost = q.popleft()

    for end in arr[start]:
        dist[end] = min(dist[end], cost)
        q.append((end, cost+1))

count = 0
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        count += 1

if not count:
    print(-1)



'''
4 4 2 1
1 2 
1 3
2 3
2 4 
'''