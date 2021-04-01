import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())  # n이 세로, m이 가로

arr = []
visited = [[0] * m for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(x, y, count):

    while q:
        x, y, count = q.popleft()
        if x == n - 1 and y == m - 1:
            print(count)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, count+1))

for i in range(n):
    arr.append(list(map(int, list(input().rstrip()))))



start = (0, 0, 1)
q = deque()
q.append(start)

bfs(0, 0, 0)
