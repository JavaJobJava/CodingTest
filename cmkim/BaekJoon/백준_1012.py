import sys;
sys.setrecursionlimit(10000)
t = int(input())


def dfs(iy, ix):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    for i in range(4):
        nx, ny = ix + dx[i], iy + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:      #상하좌우 검사해서 못가는 지역
            continue

        elif arr[ny][nx] == 1 and visited[ny][nx] == 0: #지렁이가 움직일수 있는곳
            visited[ny][nx] = 1
            dfs(ny, nx)


for _ in range(t):
    m, n, k = map(int, input().split())  # 열, 행 순서로 받음 | m이 가로, 열, x | n이 세로, 행, y |
    count = 0
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        col, row = map(int, input().split())
        arr[row][col] = 1

    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1 and visited[y][x] == 0:  # 배추가 있고 방문 안했으면
                visited[y][x] == 1  # 방문처리
                count += 1
                dfs(y, x)

    print(count)
