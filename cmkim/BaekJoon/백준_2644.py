# 이진 트리를 이용해서 풀어야하나?
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

arr = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
dist = [0 for i in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] += 1

    while q:
        v = q.popleft()  # 시작 기준이 되는 값을 잡고 시작한다.

        for i in arr[v]:  # 기준값 주변에 있는 방문하지 않은 값들을 전부 탐색한다.
            if visited[i] == 0:
                visited[i] = 1
                dist[i] = dist[v] + 1
                q.append(i)


bfs(a)
if dist[b] > 0:
    print(dist[b])
else:
    print(-1)
