import heapq

INF = int(1e9)

graph = []
distance = []


def dijkstra(start):
    global graph
    global distance

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


def solution(n, edge):
    answer = 0
    global graph
    global distance

    graph = [[] for i in range(n+1)]
    distance = [INF]*(n+1)

    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    dijkstra(1)

    maxDist = max(distance[1:])
    answer = distance[1:].count(maxDist)

    return answer
