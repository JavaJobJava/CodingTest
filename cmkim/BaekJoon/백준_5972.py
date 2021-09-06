import sys
import heapq
INF = 1e9
n, m = map(int, input().split())
arr = [[] * (n+1) for _ in range(n+1)]
dis = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #비용, 출발점
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in arr[now]: # 가려는 곳에대한 위치, 비용
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(1)
print(dis[n])