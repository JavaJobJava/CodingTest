# 결국 그냥 미로찾기 문제에서 기본 비용은 100원 처리, 코너가 발생할때마다 500원 추가로 처리하면됀다
from collections import deque

board = [[0, 0, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 1, 0, 1, 0, 1], [0, 1, 0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

q = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   #상하좌우
INF = 1000000000

def solution(board):
    answer = 0
    size = len(board)
    dp = [[INF] * size for _ in range(size)]
    visited = [[0] * size for _ in range(size)]
    visited[0][0] = 1
    if board[0][1] == 0:
        q.append((0, 0, 0, 1))
    while q:

        x, y, count, dir = q.popleft()      #dir은 진행방향 1 = 가로, -1 = 세로
        # if x == size - 1 and y == size - 1:
        #     break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == 0:
                if dp[nx][ny] > count + 6:

                    if dir == 1 and i % 4 < 2:  # 진행방향이 가로고, 다음 움직일 곳이 세로면
                        dp[nx][ny] = min(dp[nx][ny], count + 6)
                        q.append((nx, ny, count + 6, -1))
                    elif dir == -1 and i % 4 > 1:  # 진행방향이 세로고, 다음 움직일 곳이 가로면
                        dp[nx][ny] = min(dp[nx][ny], count + 6)
                        q.append((nx, ny, count + 6, 1))

                if dp[nx][ny] > count + 1:
                    if dir == 1 and i % 4 > 1:  # 진행방향이 가로고, 다음 움직일 곳도 가로면
                        dp[nx][ny] = min(dp[nx][ny], count + 1)
                        q.append((nx, ny, count + 1, 1))
                    elif dir == -1 and i % 4 < 2:  # 진행방향이 세로고, 다음 움직일 곳이 세로면
                        dp[nx][ny] = min(dp[nx][ny], count + 1)
                        q.append((nx, ny, count + 1, -1))


    answer = dp[size - 1][size - 1] * 100

    if board[1][0] == 0:
        q.append((0, 0, 0, -1))
        visited = [[INF] * size for _ in range(size)]
        visited[0][0] = 1
        dp = [[INF] * size for _ in range(size)]
        while q:

            x, y, count, dir = q.popleft()  # dir은 진행방향 1 = 가로, -1 = 세로
            # if x == size - 1 and y == size - 1:
            #     break

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == 0:
                    if dp[nx][ny] > count + 6:

                        if dir == 1 and i % 4 < 2:  # 진행방향이 가로고, 다음 움직일 곳이 세로면
                            dp[nx][ny] = min(dp[nx][ny], count + 6)
                            q.append((nx, ny, count + 6, -1))
                        elif dir == -1 and i % 4 > 1:  # 진행방향이 세로고, 다음 움직일 곳이 가로면
                            dp[nx][ny] = min(dp[nx][ny], count + 6)
                            q.append((nx, ny, count + 6, 1))

                    if dp[nx][ny] > count + 1:
                        if dir == 1 and i % 4 > 1:  # 진행방향이 가로고, 다음 움직일 곳도 가로면
                            dp[nx][ny] = min(dp[nx][ny], count + 1)
                            q.append((nx, ny, count + 1, 1))
                        elif dir == -1 and i % 4 < 2:  # 진행방향이 세로고, 다음 움직일 곳이 세로면
                            dp[nx][ny] = min(dp[nx][ny], count + 1)
                            q.append((nx, ny, count + 1, -1))

    answer = min(answer, dp[size-1][size-1] * 100)

    return answer

print(solution(board))