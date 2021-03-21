n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(0, n):
    for j in range(0, m):

        if i == 0 and j > 0:
            dp[i][j] = dp[i][j-1] + arr[i][j]
        elif i > 0 and j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        elif i > 0 and j > 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])+arr[i][j]

print(dp[n-1][m-1])

#dp table 값을 1,1 부터 이용하면 맨윗줄, 맨 왼쪽 줄 따질 필요 없다.