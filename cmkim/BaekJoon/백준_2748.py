n = int(input())

dp = [[0] for _ in range(n+1)]

dp[0], dp[1] = 0, 1


if n > 1:
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

# 이건 왜 안될까?
# dp[1], dp[2] = 1, 1
#
#
# if n>2:
#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
