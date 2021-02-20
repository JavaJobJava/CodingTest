#solved.ac
#실버2
#그래프이론
#DFS와BFS
#1260
#그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

from collections import deque

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    tmp = list(map(int,input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

for i in range(1,M):
    graph[i].sort()
visited = [False for _ in range(N+1)]

def dfs(graph,visited,V):
    print(V,end=" ")
    visited[V]=True

    for vertex in graph[V]:
        if visited[vertex] is not True:
            visited[vertex] = True
            dfs(graph,visited,vertex)

#dfs 
dfs(graph,visited,V)

#bfs
print("")
visited = [False for _ in range(N+1)]

queue = deque(graph[V])
print(V,end=" ")

while len(queue)!=0:
    if visited[queue[0]] is not True:
        visited[queue[0]] = True
        print(queue[0],end=" ")
        queue.popleft()


