#solved.ac
#실버1
#다잌스트라
#그대, 그머가 되어
#14496

import heapq
import sys 

input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억 설정
#a,b 입력 
a,b = map(int,input().split())

#N,M 입력 
N,M = map(int,input().split())
#그래프 초기화 
graph = [[] for _ in range(N+1)]

#M만큼 반복, 인접 리스트 생성 
for i in range(M):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    #시작노드에 대해서초기화 
    heapq.heappush(q,(0,start))
    distance[start] = 0
    #큐가 비어있을 때까지 반복
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost<distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))
        
dijkstra(a)

if distance[b]==INF:
    print(-1)
else:
    print(distance[b])









