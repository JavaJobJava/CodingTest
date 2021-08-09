import sys
input = sys.stdin.readline
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for i in arr2:
    start, end = 0, n
    while start <= end:
        mid = (start + end) // 2
        if 0 <= mid < n:
            if arr1[mid] < i:
                start = mid + 1
            else:
                end = mid - 1
        else:
            break
    if 0 <= end + 1 < n:
        if arr1[end + 1] == i:
            print(1, end="\n")
        else:
            print(0, end="\n")
    else:
        print(0, end="\n")

