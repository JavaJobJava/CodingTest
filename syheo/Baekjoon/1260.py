#solved.ac
#실버2
#그래프이론
#DFS와BFS
#1260
#그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

from collections import deque
import sys 
input = sys.stdin.readline

#dfs
def dfs(V):
    result_dfs.append(V)
    visited[V]=True

    for vertex in graph[V]:
        if visited[vertex] is not True:
            visited[vertex] = True
            dfs(vertex)

#bfs
def bfs(V):
    queue = deque([V])
    visited[V] =True

    while queue:
        vertex = queue.popleft()
        result_bfs.append(vertex)
        visited[vertex] = True
        for item in graph[vertex]:
            if not visited[item]:
                visited[item] = True
                queue.append(item)


N,M,V = map(int,input().split())
# 인접 리스트 그래프 생성 
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

result_dfs = []
result_bfs = []

visited = [False for _ in range(N+1)]

#dfs 
dfs(V)

#bfs
visited = [False for _ in range(N+1)]
bfs(V)

print(*result_dfs)
print(*result_bfs)
