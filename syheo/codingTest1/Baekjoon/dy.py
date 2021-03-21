
# N 행 M 열 

N,M = map(int,input().split())

dp = [[0]*(M+1) for _ in range(N+1)]

maps = []

for _ in range(N):
    maps.append(list(map(int,input().split())))

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1])+maps[i-1][j-1]


print(dp[N][M])





