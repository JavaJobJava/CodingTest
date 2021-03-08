#이 문제는 출발점에서 도착점까지의 최소거리를 구하는 문제인데 다익스트라 쓰는게 맞나? dfs, bfs가 아닌가?
from collections import deque
from sys import stdin
a, b = map(int, input().split())
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
dist = [-1]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs():
    q = deque()
    q.append(a)
    dist[a] = 0
    while q:
        x = q.popleft()
        if x == b:
            print(dist[x])
            return
        for i in arr[x]:
            if dist[i] == -1:
                q.append(i)
                dist[i] = dist[x]+1
    print(-1)

bfs()

