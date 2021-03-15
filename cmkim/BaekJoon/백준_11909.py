# 1. 오른쪽, 아래로만 이동
# 2. 출구와 같은 행이면 오른쪽으로만
# 3. 출구와 같은 열이면 아래로만
# 4. 자기보다 작은 수로만 이동 할 수 있다.
# 5. 자기 있는 칸의 수를 1늘리는 비용은 1
n = int(input())
arr = [[] * (n + 1) for _ in range(n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    arr[i] = list(map(int, input().split()))
    arr[i].insert(0, 0)

for i in range(2, n+1):             #조건 2,3 을 위해 1행과 1열을 쭉 초기화 시킨다.
    if arr[1][i] >= arr[1][i-1]:
        dp[1][i] += dp[1][i-1] + arr[1][i] - arr[1][i - 1] + 1

    else:
        dp[1][i] = dp[1][i - 1]

    if arr[i][1] >= arr[i-1][1]:
        dp[i][1] += dp[i-1][1] + arr[i][1] - arr[i - 1][1] + 1

    else:
        dp[i][1] = dp[i - 1][1]

for i in range(2, n+1):
    for j in range(2, n+1):
        down, right = 0, 0
        if arr[i][j] >= arr[i-1][j]:
            down = arr[i][j] - arr[i-1][j] + 1
        if arr[i][j] >= arr[i][j-1]:
            right = arr[i][j] - arr[i][j-1] + 1
        dp[i][j] = min(dp[i-1][j] + down, dp[i][j-1] + right)

print(dp[n][n])
