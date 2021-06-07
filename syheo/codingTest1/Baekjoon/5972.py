#solved.ac
#골드5
#?
#택배 배송
#5972

#bfs+다익스트라 일부 

from collections import deque

def bfs(N,dp):
    q = deque([(1,0)]) #현재 위치, 여물 수 
    dp[1]=0
    while q:
        print(q)
        node, cost = q.popleft()
        if dp[node]<cost:
            continue
        for info in graphs[node]:
            dest = info[0]
            c = info[1]
            if dp[dest]>cost+c:
                dp[dest]=cost+c
                q.append((dest,cost+c))


N,M = map(int,input().split())    
INF = int(1e9)
graphs = [[] for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    graphs[a].append((b,c))
    graphs[b].append((a,c))

dp = [INF for _ in range(N+1)]

bfs(N,dp)

print(dp[N])

