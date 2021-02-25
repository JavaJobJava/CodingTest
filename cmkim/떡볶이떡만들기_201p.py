n, m = map(int, input().split())

arr = list(map(int, input().split()))
start = 0
end = max(arr)
#어디서 자를지를 이진 탐색을 통해 정한다

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            sum += x - mid
    if sum < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)