#solved.ac
#실버2
#DFS&BFS
#연결 요소의 갯수
#11724

#BFS 풀이
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    if visited[start]:
        return False
    q = deque([start])

    while q:
        v = q.popleft()
        visited[v]=True
        
        for edge in edges[v]:
            if not visited[edge]:
                visited[edge]=True
                q.append(edge)
    return True

N,M = map(int,input().split())
#인접리스트 
edges = [[] for _ in range(N+1)]
cnt = 0
for i in range(M):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)
visited = [False for _ in range(N+1)]

for i in range(1,N+1):
    if bfs(i):
        cnt+=1

print(cnt)
    


