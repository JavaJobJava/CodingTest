#solved.ac
#골드5
#?
#택배 배송
#5972

#다익스트라 
import sys
import heapq
input = sys.stdin.readline

def bfs(N,dp):
    q = []
    heapq.heappush(q,(0,1)) #여물 수, 현재 위치  
    dp[1]=0
    while q:
        cost, node = heapq.heappop(q)
        if dp[node]<cost:
            continue
        for info in graphs[node]:
            dest = info[0]
            c = info[1]
            if dp[dest]>cost+c:
                dp[dest]=cost+c
                heapq.heappush(q,(cost+c,dest))


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