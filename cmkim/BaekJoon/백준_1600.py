from collections import deque

dx, dy = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1] #시계방향
dx2, dy2 = [-1, 1, 0, 0], [0, 0, -1, 1] #상하좌우

k = int(input())
m, n = map(int, input().split())  # m이 가로 n이 세로
arr = []
visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
visited[0][0][0] = 1

for i in range(n): #맵 정보 입력
    arr.append(list(map(int, input().split())))

q = deque()
q.append((0, 0, 0, 0)) # x좌표, y좌표, 이동비용, 말이 움직인 횟수


def bfs():  # x -> row | y -> col
    while q:
        x, y, count, action = q.popleft() # x, y 는 좌표 정보 | count는 움직인 횟수 | action은 말의 움직임을 쓴 횟수
        if x == n - 1 and y == m - 1: #목적지 도착
            print(count)
            return

        for i in range(4):      #상하좌우 이동
            nx = x + dx2[i]
            ny = y + dy2[i]
            if action >= k:     #말의 움직임을 다 쓴 경우 visited에 최대 사용가능한 말의 움직임 k로 저장한다.
                if 0 <= nx < n and 0 <= ny < m and visited[k][nx][ny] == 0 and arr[nx][ny] == 0:
                    visited[k][nx][ny] = 1
                    q.append((nx, ny, count + 1, action))
            else:               #말의 움직임을 다 안 쓴 경우 현재 사용한 말의 움직임을 visited에 저장
                if 0 <= nx < n and 0 <= ny < m and visited[action][nx][ny] == 0 and arr[nx][ny] == 0:
                    visited[action][nx][ny] = 1
                    q.append((nx, ny, count + 1, action))

        if action < k:          #말의 움직임 이동 (시계방향)
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[action + 1][nx][ny] == 0 and arr[nx][ny] == 0:
                    visited[action + 1][nx][ny] = 1
                    q.append((nx, ny, count + 1, action + 1))
    return -1 #큐를 다 돌렸는데 목적지 도착해서 return 되지 않은 경우 -1 return


if bfs() == -1:  # 말의 이동
    print(-1)
