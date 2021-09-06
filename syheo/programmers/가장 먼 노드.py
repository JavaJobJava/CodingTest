#프로그래머스 
#고득점 Kit
#그래프
#level3
#가장 먼 노드

from collections import deque
import heapq

def dijkstra(n,edge,graphs):
    rst = 0
    INF = int(1e9)
    distance = [INF for _ in range(n+1)]
    distance[0] = 0 
    
    q = [(0,1)]
    distance[1] = 0
    
    while q:
        cnt,node = heapq.heappop(q)
        if distance[node]<cnt:
            continue
        for v in graphs[node]:
            cost = cnt + 1
            if cost < distance[v]:
                distance[v]=cost
                heapq.heappush(q,(cost,v))
                
    maxCost = max(distance)
    
    for i in range(1,n+1):
        if maxCost == distance[i]:
            rst+=1
    return rst
        

def solution(n, edge):
    answer = 0
    graphs = [[]*(n+1) for _ in range(n+1)]
    for i in range(len(edge)):
        graphs[edge[i][0]].append(edge[i][1])
        graphs[edge[i][1]].append(edge[i][0])
        
    answer = dijkstra(n,edge,graphs)
    
    return answer