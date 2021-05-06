import sys, heapq

n, m = map(int, input().split())
INF = 1000000000
d = [[INF]*(n+1) for _ in range(n+1)]
result = 0

for i in range(m):
    a, b, dist = map(int, input().split())
    d[a][b] = dist
    d[b][a] = dist

for i in range(n):
    d[i+1][i+1] = 0

def dijkstra1(start, dest): # 달빛여우
    q = []
    distance = [INF] * (n+1)
    distance[start] = 0
    heapq.heappush(q, [0, start])

    while(q):
        cur_distance, cur = heapq.heappop(q)

        for i in range(1, n+1):
            if 0 < d[cur][i] < INF:
                if d[cur][i] + cur_distance < distance[i]:
                    distance[i] = d[cur][i] + cur_distance
                    heapq.heappush(q, [distance[i], i])

    return distance[dest]

def dijkstra2(start, dest): #달빛늑대
    q = []
    distance = [[INF] * (n + 1) for _ in range(2)] # distance[0] 빠른도착 , distance[1] 느린 도착
    distance[start][start] = 0
    heapq.heappush(q, [0, start, 1]) # 3번째 인자를 추가, 1 = 두배의 속력, -1 = 절반의 속력
    result_distance = [INF] * (n+1)

    while(q):
        cur_distance, cur, condition = heapq.heappop(q)

        for i in range(1, n+1):
            if 0 < d[cur][i] < INF:
                if condition == 1:
                    if (d[cur][i]/2) + cur_distance < distance[0][i]:
                        distance[0][i] = (d[cur][i] / 2) + cur_distance
                        heapq.heappush(q, [distance[0][i], i, -1])

                elif condition == -1:
                    if (d[cur][i] * 2) + cur_distance < distance[1][i]:
                        distance[1][i] = (d[cur][i] * 2) + cur_distance
                        heapq.heappush(q, [distance[1][i], i, 1])

    for i in range(1, n+1):
        result_distance[i] = min(distance[0][i], distance[1][i])

    return result_distance[dest]


for i in range(2, n+1):
    if dijkstra1(1, i) < dijkstra2(1, i):
        result += 1

print(result)
