from collections import deque

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


way = {'|': [0, 1], '-': [2, 3], '+': [0, 1, 2, 3], '1': [1, 3], '2': [0, 3], '3': [0, 2],
       '4': [1, 2]}



def bfs(x, y):
    global ax, ay #정답 파이프의 위치를 저장할 변수

    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        dir = way[arr[x][y]] #파이프의 모양에 따라 상하좌우중 어디로 갈지 정한다.

        for i in dir:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                #print(arr[nx][ny])
                if arr[nx][ny] != '.': # 파이프가 있는 곳이라면 방문해서 진행한다.
                    if arr[nx][ny] != 'Z':
                        visited[nx][ny] = 1
                        q.append((nx, ny))
                else:                   # 진행방향대로 진행했는데 파이프가 없다면 정답파이프의 위치이다.
                    ax, ay = nx, ny
                    #print('ax, ay = ', ax, ay)
                    for j in range(4):
                        cx = nx + dx[j]
                        cy = ny + dy[j]
                        if 0 <= cx < r and 0 <= cy < c and arr[cx][cy] != '.' and arr[cx][cy] != 'M' and arr[cx][cy] != 'Z': # 연결된 통로 구하기
                            if can_move(cx, cy, nx, ny):
                                check.append(j)
                    return

def firstblock(x, y): # 첫번째 파이프를 찾는 함수
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != '.':
            visited[x][y] = 1
            return nx, ny

def can_move(sx, sy, ex, ey): #연결된 파이프를 찾기위해 sx, sy -> ex, ey 이동이 가능한지 찾는 함수
    dir = way[arr[sx][sy]]
    flag = False
    for i in dir:
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < r and 0 <= ny < c and nx == ex and ny == ey:
            flag = True
    return flag

r, c = map(int, input().split())

visited = [[0]*c for _ in range(r)]
check = [] #지워진 공간에서 어디로 이어질지 저장
#arr = []
# for i in range(r):
#     arr.append(list(input()))
arr = [list(input()) for _ in range(r)]

# for i in range(r):
#     print(arr[i])


for i in range(r):
    for j in range(c):
        if arr[i][j] == 'M':
            x, y = i, j
            visited[x][y] = 1


fx, fy = firstblock(x, y)
#print('fx, fy = ', fx, fy)
bfs(fx, fy)


#print(check) # 0 1 2 3 = 상 하 좌 우

if check == [0, 1]:
    result = '|'
elif check == [2, 3]:
    result = '-'
elif check == [0, 1, 2, 3]:
    result = '+'
elif check == [1, 3]:
    result = '1'
elif check == [0, 3]:
    result = '2'
elif check == [0, 2]:
    result = '3'
elif check == [1, 2]:
    result = '4'

print(ax+1, ay+1, result)

'''
3 7
.14....
.M.Z...
..23...

3 5
..1-M
.Z+4.
..2..

3 7
.......
.M-.Z..
.......

2 4
M1-Z
2-..

2 3
M.Z
2.3

'''

