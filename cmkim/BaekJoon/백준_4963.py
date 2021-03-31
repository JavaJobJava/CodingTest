from collections import deque

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    else:
        arr = [[0] * (w+1) for _ in range(h+1)]
        visited = [[0] * (w+1) for _ in range(h+1)]
        for i in range(h):
            arr[i] = list(map(int, input().split()))
        q = deque()
        count = 0
        for row in range(h):
            for col in range(w):
                if arr[row][col] == 1 and visited[row][col] == 0:

                    q.append((col, row))
                    count += 1
                    visited[row][col] = 1


                    while q:
                        x, y = q.popleft()  # col, row 순서
                        for index in range(8):
                            nx = x + dx[index]
                            ny = y + dy[index]
                            if 0 <= nx < w and 0 <= ny < h:
                                if visited[ny][nx] == 0 and arr[ny][nx] == 1:
                                    visited[ny][nx] = 1
                                    q.append((nx, ny))
        print(count)