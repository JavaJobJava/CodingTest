from collections import deque

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

way = {'M': [0, 1, 2, 3], '|': [0, 1], '-': [2, 3], '+': [0, 1, 2, 3], '1': [1, 3], '2': [0, 3], '3': [0, 2], '4': [1, 2]}

def bfs(x, y):
    dir = way[arr[x][y]]
    for i in dir:
        nx = x + dx[i]
        ny = y + dy[i]



r, c = map(int, input().split())
arr = []

for i in range(r):
    arr.append(list(input()))

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'M':
            x, y = i, j
# for i in range(r):
#     print(arr[i])

bfs(x, y)
