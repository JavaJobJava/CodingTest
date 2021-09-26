import sys
from collections import deque

input = sys.stdin.readline

odd = [(-1, 1), (0, 1), (1, 1), (1, 0), (0, -1), (-1, 0)]  # 행, 렬 기준으로함 정각부터 정시계방향으로 순환
even = [(-1, 0), (0, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def bfs(x, y):
    q = deque([(x, y)])
    count = 0
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        dir = even if x % 2 == 0 else odd
        for i in range(6):
            dx, dy = dir[i][0], dir[i][1]
            nx, ny = x + dx, y + dy

            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if arr[nx][ny] == 1:
                    count += 1
                elif arr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return count


w, h = map(int, input().split())  # 열, 행 순서로 입력
arr = [[0] * (w + 2)]
visited = [[0] * (w + 2) for _ in range(h + 2)]
for i in range(h):
    arr.append([0] + list(map(int, input().split())) + [0])
arr.append([0 for _ in range(w + 2)])

# for i in range(h+2):
#     print(arr[i])

print(bfs(0, 0))
