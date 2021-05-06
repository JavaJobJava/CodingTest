n = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
dp = [[0]*(n+1) for _ in range(n+1)]
count = [0] * (n+1)
for i in range(n):
    num = int(input())
    for j in range(n):
        arr[i][j] = num // (10 ** (n - j - 1))
        num -= arr[i][j] * (10 ** (n - j - 1))

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

# print(arr)
# print(dp)

for size in range(1, n+1):
    for i in range(size, n + 1):
        for j in range(size, n + 1):
            if dp[i][j] - dp[i][j-size] - dp[i-size][j] + dp[i-size][j-size] == size ** 2:
                count[size] += 1

for i in range (1, n+1):
    print('size[', i, ']:', count[i])

'''
4
1110
1110
0110
0000
'''