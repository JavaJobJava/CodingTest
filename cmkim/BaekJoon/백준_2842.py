import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0, -1, 1, 1, -1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

N = int(input())
map = [list(map(str, input().rstrip())) for _ in range(N)]
height = [[int(x) for x in input().split()] for _ in range(N)]
visited = [[0]*N for _ in range(N)]
houses = []
n_house = 0

# print(map)
# print(height)

def bfs(x, y, count):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    count += 1
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                if height[nx][ny] < low:
                    low = height[nx][ny]
                if height[nx][ny] < high:
                    high = height[nx][ny]
                q.append([nx, ny])




for i in range(N):
    for j in range(N):
        if map[i][j] == 'P':
            sx, sy = i, j  #시작위치
            houses.append([i, j])
            n_house += 1
        if map[i][j] == 'K':
            houses.append([i, j])
            n_house += 1
#print(type(height[1][1]))
# print(houses)
low, high = 1000000, 0


for i in range(n_house):

    if height[houses[i][0]][houses[i][1]] < low:
        low = height[houses[i][0]][houses[i][1]]

    if height[houses[i][0]][houses[i][1]] > high:
        high = height[houses[i][0]][houses[i][1]]

print('low, high = ', low, high)