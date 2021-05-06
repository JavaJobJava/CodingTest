n, m = map(int, input().split())

arr = [[0]*n for _ in range(m)]
dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(m):
    arr[i] = list(map(int, input().split()))

for i in range(m):
    for j in range(n):
        dp[i+1][j+1] = arr[i][j] + max(dp[i][j+1], dp[i+1][j])

print(dp[m][n])