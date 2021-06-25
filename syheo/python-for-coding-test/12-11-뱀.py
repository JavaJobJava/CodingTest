#CH12 구현 기출
#예제 12-11
#뱀
#백준 3190
#골드 5

# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

from collections import deque

#N:board size, K:apple count
N = int(input())
K = int(input())

#0: 빈칸, 1:사과, 2:뱀 몸통
maps = [[0]*(N+1) for _ in range(N+1)]
#사과 입력 
for i in range(K):
    a,b = map(int,input().split())
    maps[a][b]=1

#방향전환 입력 
opCnt = int(input())
ops = deque([])
for i in range(opCnt):
    a,b = map(str,input().split())
    ops.append((int(a),b))

time = 0
moves = [(0,1),(1,0),(0,-1),(-1,0)] #우하좌상
direction = 0
row , col = 1, 1
snake = deque([(row,col)])
maps[row][col]=2

while True:
    #시간 1초 증가
    time += 1
    #이동
    row = row+moves[direction][0]
    col = col+moves[direction][1]
    if (row<=0 or row>N) or (col<=0 or col>N) or maps[row][col]==2:
        gameover = True
        break
    else:
        snake.append((row,col))
        if maps[row][col]==0:
            a,b = snake.popleft()
            maps[a][b]=0
        maps[row][col]=2
    #명령 시간이 되었다면 
    if ops and ops[0][0]==time:
        X,C = ops.popleft()
        if C=='L':
            direction=direction-1 if direction>0 else 3
        elif C=='D':
            direction=direction+1 if direction<3 else 0


print(time)

