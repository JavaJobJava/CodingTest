import sys

sys.setrecursionlimit(10 ** 9)

dir = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}


def dfs(x, y):
    if 0 > x or x >= n or 0 > y or y >= m:  # 탈출
        return True

    if arr[x][y] == 'true':  # 탈출 확정된 곳
        return True
    elif arr[x][y] == 'false':  # 탈출 불가능 확정된 곳
        return False

    if visited[x][y]:
        return False
    else:
        visited[x][y] = 1
        dx, dy = dir[arr[x][y]]
        nx = x + dx
        ny = y + dy

        result = dfs(nx, ny)
        arr[x][y] = 'true' if result else 'false'
        return result


n, m = map(int, input().split())
arr = []
visited = [[0] * m for _ in range(n)]
for i in range(n):
    arr.append(list(input()))

# for i in range(n):
#     print(arr[i])

# ax, ay = dir[arr[0][0]]
# print('ax, ay = ', ax, ay)

count = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y):
            count += 1

print(count)
