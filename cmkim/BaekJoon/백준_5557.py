n = int(input())

arr = list(map(int, input().split()))
#print(arr)
#print(arr.pop())
#print(arr)
result = arr.pop()
#arr.sort()

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n-1):
    dp[i] = dp[i-1] + arr[i]

print(dp)
