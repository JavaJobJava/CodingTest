from collections import deque

dx, dy = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]  # 시계방향
INF = 999999


def bfs(x, y, count):  # x -> row | y -> col
    while q:
        x, y, count = q.popleft()
        if x == dest[0] and y == dest[1]:
            print(dp[x][y])
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dp[nx][ny] = min(dp[nx][ny], count + 1)
                q.append((nx, ny, count + 1))


T = int(input())

for _ in range(T):
    n = int(input())
    arr = [[0] * n for __ in range(n)]
    dp = [[INF] * n for __ in range(n)]
    visited = [[0] * n for __ in range(n)]
    visited[0][0] = 1
    start = list(map(int, input().split()))
    dest = list(map(int, input().split()))

    q = deque()
    q.append((start[0], start[1], 0))
    if start == dest:
        print(0)
    else:
        bfs(start[0], start[1], 0)
