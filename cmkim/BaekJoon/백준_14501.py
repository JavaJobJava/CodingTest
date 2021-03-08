n = int(input())
t = []
p = []
dp = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)

dp.append(0)

for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])
# arr = [[0]*2 for i in range(n+1)]
# #arr1 = [[0] for i in range(n+1)] #걸리는 시간
# #arr2 = [[0] for i in range(n+1)] #얻는 비용
#
# dp = [0 for i in range(n+1)]
#
# maxdp = 0
# result = -999999
# for i in range(1, n+1):
#     arr[i][0], arr[i][1] = map(int, input().split())
#     #arr1[i], arr2[i] = map(int, input().split())
#
# #for i in range(1, n+1):
# #    print(arr)
#
#
#
# for i in range(1, n+1):
#     #dp[i] = maxdp
#     if i + arr[i][0] - 1 < n:
#         # print('i = ', i)
#         # print('dp[i+arr[i][0] - 1] = ', dp[i + arr[i][0] - 1])
#         # print('dp[i] = ', dp[i])
#         # print('arr[i][1] = ', arr[i][1])
#         dp[i + arr[i][0] - 1] = max(dp[i+arr[i][0] - 1], dp[i] + arr[i][1])
#         #print('dp[4] = ', dp[4])
#
#     #maxdp = max(maxdp, dp[i])
#
#
# # for i in range(1, n+1):
# #     print(dp[i])
# # for i in range(1, n+1):
# #     print(dp[i][0])
#
# for i in range(1, n+1):
#     result = max(result, dp[i])
#     print('result, dp[i] = ', result, dp[i])
#
# print(result)
