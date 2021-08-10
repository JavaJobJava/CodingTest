#solved.ac
#골드4
#다익스트라
#서강 그라운드
#14938

#bfs 풀이 

from collections import deque

#지역의 개수,수색 범위, 길의 개수
n,m,r = map(int,input().split())

itemList = [0]+list(map(int,input().split()))
graph = [[] for _ in range(n+1)]

for i in range(r):
    tmp = list(map(int,input().split()))
    graph[tmp[0]].append((tmp[1],tmp[2]))
    graph[tmp[1]].append((tmp[0],tmp[2]))

def bfs(start):
    sum = itemList[start]
    q = deque()
    q.append((start,0))
    visited[start] = True
    while q:
        v, dist = q.popleft()
        for info in graph[v]:
            node = info[0]
            cost = info[1]
            #거리 만족 시
            if dist+cost <= m:
                #방문안한 노드만 더해줌 
                if not visited[node]:
                    sum += itemList[node]
                q.append((node,dist+cost))
                visited[node] = True
    return sum

maxItem = 0

for i in range(1,n+1):
    visited = [False for _ in range(n+1)]
    maxItem = max(maxItem,bfs(i))
print(maxItem)

