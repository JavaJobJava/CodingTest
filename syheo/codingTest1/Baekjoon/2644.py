#solved.ac
#실버2
#BFS
#촌수 계산
#2644

#두 정점 사이의 간선의 수가 촌수임 
#BFS로 접근하면서 간선의 수 카운트 

import sys, queue
input = sys.stdin.readline

#입력 
n = int(input())
#두 사람 입력 
a,b = map(int,input().split())
result = -1
#부모관계 입력 
m = int(input())
#그래프 이차원 리스트 
graph = [[] for _ in range(n+1)]
#방문 체크 리스트 
visited = [False for _ in range(n+1)]

#그래프 인접리스트 생성
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
#큐에 (번호,기준으로부터 간선 수)
q = queue.deque()
for _ in graph[a]:
    q.append((_,1))

#BFS
while(q):
    #방문 처리 
    v = q.popleft()
    visited[v[0]]= True
    #탈출 조건 
    if v[0] == b:
        result = v[1]
        break
    #연결 간선이 있을 경우 
    for _ in graph[v[0]]:
        if not visited[_]:
            q.append((_,v[1]+1))
        
print(result)
