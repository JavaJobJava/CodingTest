import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n, e = map(int, input().split())

graph = [[] for i in range(n + 1)]


arr = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c)) # a부터 b까지의 거리가 c이다.
    arr[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

first = dijkstra(1)
second = dijkstra(v1)
third = dijkstra(v2)
if min(first[v1]+second[v2]+third[n], first[v2]+third[v1]+second[n])<INF:
    print(min(first[v1]+second[v2]+third[n], first[v2]+third[v1]+second[n]))
else:
    print('-1')