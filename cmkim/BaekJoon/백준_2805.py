n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in range(len(arr)):
        if arr[i] - mid > 0:
            sum += arr[i] - mid

    if sum == m:
        end = mid
        break

    elif sum < m:
        end = mid - 1

    else:
        start = mid + 1

print(end)
'''
4 8
20 15 10 17
'''