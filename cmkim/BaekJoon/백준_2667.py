from collections import deque

n = int(input())
arr = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0 , 0], [0, 0, -1, 1] # 상하좌우 순
answer = []

def bfs():
    count = 1
    while q:
        x, y = q.popleft()  # x는 row, y는 col
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx, ny))
                count += 1
    return count


for i in range(n):
    arr[i] = list(map(int, input().rstrip()))

q = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] and visited[i][j] == 0:
            q.append((i, j))
            result = bfs()
            if result:
                answer.append(result)

print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])
