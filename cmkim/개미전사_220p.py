n = int(input())

arr = list(map(int, input().split()))

dp = [0] * 101

dp[1] = arr[1]
dp[2] = max(arr[1], arr[2])
for i in range(3, n+1):
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

print(dp[n])
