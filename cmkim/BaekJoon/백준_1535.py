import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split())) #체력
J = list(map(int, input().split())) #기쁨
L, J = [0] + L, [0] + J     #1번 인덱스부터 사용하기 위해서 맨 앞에 땡겨준다
dp = [[0 for _ in range(101)] for _ in range(21)]

for i in range(1, n+1):
    for j in range(1, 101):
        if L[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i])
        else: dp[i][j] = dp[i-1][j]

print(dp[n][99])
