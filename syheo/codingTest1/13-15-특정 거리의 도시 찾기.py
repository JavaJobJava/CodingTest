#CH13 BFSDFS기출
#예제 13-15
#특정거리의 도시찾기
#백준 18352
#실버 2 

from collections import deque
import sys
input = sys.stdin.readline

N,M,K,X = map(int,input().split())

edges = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
#간선 정보 입력 받기
for i in range(M):
    a,b = map(int,input().split())
    edges[a].append(b)

def bfs():
    answer = []
    q = deque([])
    q.append((X,0)) #현재노드, 이동 거리 
    visited[X]=True
    while q:
        node, cnt = q.popleft()
        if cnt==K:
            answer.append(node)
        for next in edges[node]:
            if not visited[next]:
                q.append((next,cnt+1))
                visited[next]=True
    return answer 

result = bfs()
result.sort()
if len(result)==0:
    print(-1)
else:
    for res in result:
        print(res)