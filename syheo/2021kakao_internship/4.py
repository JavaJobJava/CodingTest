# n = 3
# start = 1
# end = 3
# roads = [[1, 2, 2], [3, 2, 3]]
# traps = [2]
n=4
start =1
end = 4 
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

INF = int(1e9)

from collections import deque
import heapq

def change_direction2(target,graph,n):
    changed_graph = graph[:]
    appendList = []
    for i in range(len(changed_graph)):
        info = changed_graph[i]
        if info[0]==target or info[1]==target:
            changed_graph[i]=(info[1],info[0],info[2])
    return changed_graph

def change_direction(target,graph,n):
    changed_graph = graph[:]
    changedList = []
    for i in range(len(changed_graph[target])):
        info = changed_graph[target][i]
        if info[2]==1:
            changed_graph[target][i]=(info[0],info[1],-1)
        elif info[2]==-1:
            changed_graph[target][i]=(info[0],info[1],1)
            changedList.append(info[0])

    for i in changedList:
        for j in range(len(changed_graph[i])):
            info = changed_graph[i][j]
            if info[0]==target:
                if info[2]==1:
                    changed_graph[i][j]=(info[0],info[1],-1)
                elif info[2]==-1:
                    changed_graph[i][j]=(info[0],info[1],1)
                    changedList.append(info[0])
        
    return changed_graph

def dijkstra(start,end,traps,graph,n,distances):
    q = []
    heapq.heappush(q,(0,start,graph[:]))
    distances[start].append(0)
    while q: 
        dist, now ,changed_graph = heapq.heappop(q)
        if min(distances[now]) < dist:
            continue
        for i in changed_graph[now]:   
            if i[2]==1:
                cost = dist + i[1]
                tmp_dst = distances[i[0]][now]
                if cost < tmp_dst:
                    distances[i[0]][now]=cost
                    if i[0] in traps:
                        heapq.heappush(q,(cost,i[0],change_direction(i[0],changed_graph,n)))
                    else:
                        heapq.heappush(q,(cost,i[0],change_direction(i[0],changed_graph,n)))
                    
    
def bfs(start,end,traps,graph,n):
    q = deque()
    cntList = []
    #start,end,cost 
    q.append((start,end,0,graph[:],''))
    while q:
        a,b,cost,change_map,visited = q.popleft()
        for info in change_map[a]:
            #print(a,b,cost,change_map,visited)
            if str(a)+str(info[0]) not in visited and info[2]==1:
                v = info[0] 
                c = info[1]
                if v==end:
                    return cost+c
                else:
                    if v in traps:
                        q.append((v,end,cost+c,change_direction(v,change_map,n),visited+str(v)))
                    else:
                        q.append((v,end,cost+c,change_map,visited+str(v)))
        
    return min(cntList)



def solution(n, start, end, roads, traps):
    graph = [[] for i in range(n+1)]
    distance = [[INF for _ in range(n+1)] for i in range(n+1)]
    distances = [[ INF for i in range(n+1)] for _ in range(n+1)]

    #visited = [[[False for j in range(n+1)] for i in range(n+1)] for _ in range(n+1)]
    for road in roads:
        #1-> , -1<-
        if distance[road[0]][road[1]]>road[2]:
            graph[road[0]].append((road[1],road[2],1))
            distance[road[0]][road[1]]=road[2]
            graph[road[1]].append((road[0],road[2],-1))
            distance[road[1]][road[0]]=road[2]
    #다익스트라 알고리즘 수행 
    dijkstra(start,end,traps,graph,n,distances)
    print(distances)
    return min(distances[end])


print(solution(n,start,end,roads,traps))