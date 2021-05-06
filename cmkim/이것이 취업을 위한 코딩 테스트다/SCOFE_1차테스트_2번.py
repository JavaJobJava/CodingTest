n = int(input())
num = int(input())
arr = [0]* (n+2)
flag = 0

for i in range(n):
    arr[i] = num // (10**(n-i-1))
    num -= arr[i] * (10**(n-i-1))
    if flag < arr[i]:
        flag = arr[i]
        start = i

dp = [0] * (n+2)
# dp[0] = arr[0]
# dp[1] = arr[0]*1
#print('start = ', start)
if arr[start+1]:
    dp[start+1] = arr[start+1]
if arr[start+2]:
    dp[start+2] = arr[start+2] + dp[start+1]

for i in range(start+3, n):
    if arr[i]:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1])

# print(arr)
# print(dp)