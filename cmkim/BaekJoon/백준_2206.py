import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
arr = []  # 맵 정보
arr.append([1 for _ in range(m + 1)])
visited = [[[0] * (m + 1) for _ in range(n + 1)] for __ in range(2)]

for i in range(1, n + 1):
    arr.append(list(map(int, input().strip())))
    arr[i].insert(0, 1)


def bfs():
    q = deque()
    q.append((1, 1, 1, 0))  # x, y, cost, 벽부순지에 대한 여부
    visited[0][1][1] = 1
    visited[1][1][1] = 1
    while q:
        x, y, c, flag = q.popleft()
        # visited[0][x][y] = c
        # visited[1][x][y] = c  <- 이렇게 두개의 배열다 초기화 시키는 방법은 왜 시간초과가 날까?
        # if x == n and y == m:
        #     print(visited[flag][x][y], flag)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx <= n and 0 < ny <= m and arr[nx][ny] == 0 and not visited[flag][nx][ny]:
                q.append((nx, ny, c + 1, flag))
                visited[flag][nx][ny] = visited[flag][x][y] + 1
            if 0 < nx <= n and 0 < ny <= m and arr[nx][ny] == 1 and flag == 0:
                q.append((nx, ny, c + 1, 1))
                visited[flag+1][nx][ny] = visited[flag][x][y] + 1


bfs()

result = 0
for i in range(2):
    if visited[i][n][m]:
        result = visited[i][n][m]
if result:
    print(result)
else:
    print(-1)
