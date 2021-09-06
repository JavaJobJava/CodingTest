from _collections import deque
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [list(map(str, input())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]   #dp 배열추가
# q = deque()
# q.append((0, 0, 1))# x, y 좌표와 움직인 횟수
result = 0         # 가장 큰 값을 저장해줄 변수

def bfs(x, y, count):
    global result
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i] * int(arr[x][y])
        ny = y + dy[i] * int(arr[x][y])

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'H' and dp[nx][ny] < count + 1: #적은 이동횟수는 무시하는 조건 추가
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = count + 1
                visited[nx][ny] = 1
                bfs(nx, ny, count+1)
                visited[nx][ny] = 0

bfs(0, 0, 0)
print(result + 1)

# while q:
#     x, y, count = q.popleft()
#
#     if count > n*m: #무한 반복될때 종료조건
#         print(-1)
#         quit()
#     for i in range(4):
#         nx = x + dx[i] * int(arr[x][y])
#         ny = y + dy[i] * int(arr[x][y])
#
#         if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'H' and visited[nx][ny] < count: #적은 이동횟수는 무시하는 조건 추가
#             q.append((nx, ny, count+1))
#             visited[nx][ny] = count
#
#
# for i in range(n):
#     for j in range(m):
#         result = max(result, visited[i][j])
#
# if result < n*m:
#     print(result + 1)
# else:
#     print(-1)


# bfs 함수 따로 뽑아서 하는거랑 메인에서 q 구현해서 하는거랑 대체 무슨 차이?
# 밑에 1크게 시작하는거랑 무슨차이?
'''
def bfs(x, y, count):
    global result
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i] * int(arr[x][y])
        ny = y + dy[i] * int(arr[x][y])

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 'H' and dp[nx][ny] < count: #적은 이동횟수는 무시하는 조건 추가
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = count +1
                visited[nx][ny] = 1
                bfs(nx, ny, count+1)
                visited[nx][ny] = 0

bfs(0, 0, 1)
print(result)
'''