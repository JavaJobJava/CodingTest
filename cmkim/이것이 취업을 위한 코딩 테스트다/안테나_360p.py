# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
#
# print(a[(n - 1) // 2])

n = int(input())
arr = []
arr = list(map(int, input().split()))
arr.sort()
answer = 0
for i in range(n):
    answer += arr[i]

answer /= n

min_v = 1e9
min_index = 0


for i in reversed(range(n)):
    if min_v >= abs(arr[i]-answer):
        min_v = min(min_v, abs(arr[i] - answer))
        min_index = i


print(arr[min_index])

'''
4
1 5 6 10
'''
#1 2 10 11