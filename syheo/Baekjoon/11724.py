#solved.ac
#실버2
#DFS&BFS
#연결 요소의 갯수
#11724

#dfs 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(start):
    if visited[start]:
        return False
    visited[start]=True

    for v in edges[start]:
        if not visited[v]:
            dfs(v)
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
    if dfs(i):
        cnt+=1

print(cnt)
    


