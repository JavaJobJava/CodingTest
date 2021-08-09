from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def water():
    qlen = len(wq)
    while qlen:
        x, y = wq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if a[nx][ny] == '.':
                    a[nx][ny] = '*'
                    wq.append([nx, ny])
        qlen -= 1

def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1
    while q:
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if a[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny])
                    elif a[nx][ny] == 'D':
                        print(visited[x][y])
                        return
            qlen -= 1
        water()

    print("KAKTUS")
    return


r, c = map(int, input().split())
a = [list(map(str, input())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
q, wq = deque(), deque()

for i in range(r):
    for j in range(c):
        if a[i][j] == 'S':
            x1, y1 = i, j
            a[i][j] = '.'
        elif a[i][j] == '*':
            wq.append((i, j))

water()
bfs(x1, y1)



