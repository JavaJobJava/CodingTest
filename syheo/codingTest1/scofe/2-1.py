import sys
sys.setrecursionlimit(10**9)

N = int(input())
path = list(input())
dp=[0 for i in range(N)]
dp[0]=1
for i in range(N):
    if i<=N-2:
        if int(path[i+1])==1:
            dp[i+1]+=dp[i]
    if i<=N-3:
        if int(path[i+2])==1:
            dp[i+2]+=dp[i]
#print(dp)
print(dp[N-1])