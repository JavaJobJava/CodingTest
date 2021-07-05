from _collections import deque



dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

def solution(grid):
    answer = 0
    row = len(grid)
    col = len(grid[0])
    map = [[1e9] * col for _ in range(row)]
    map[0][0] = grid[0][0]
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if map[x][y] + grid[nx][ny] < map[nx][ny]:
                    map[nx][ny] = map[x][y] + grid[nx][ny]
                    q.append((nx, ny))


    answer = map[row-1][col-1]


    return answer