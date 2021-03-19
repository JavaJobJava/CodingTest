n = int(input())
arr = [[0]*2 for i in range(n+1)]

for i in range(1, n+1):
    arr[i][0], arr[i][1] = map(int, input().split())

