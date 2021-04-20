#solved.ac
#실버2
#DFS&BFS
#단지 번호 붙이기
#2667

import sys
from collections import deque
input = sys.stdin.readline

moves = [(1,0),(0,1),(-1,0),(0,-1)]

def bfs(row,col,N):
    cnt = 0
    #시작 좌표 큐에 넣어줌 
    q = deque([(row,col)])
    visited[row][col]=True
    while q:
        row,col = q.popleft()
        cnt+=1
        for move in moves:
            r = row+move[0]
            c = col+move[1]
            if 0<=r<=N-1  and 0<=c<=N-1:
                if maps[r][c]==1 and not visited[r][c]:
                    q.append((r,c))
                    visited[r][c]=True
    return cnt 
                

N = int(input())
visited=[[False]*N for i in range(N)]
maps = []
cntList = []
#입력 
for i in range(N):
    maps.append(list(map(int,list(input().rstrip()))))

#bfs 방문
for i in range(N):
    for j in range(N):
        if not visited[i][j] and maps[i][j]:
            cnt = bfs(i,j,N)
            cntList.append(cnt)

cntList.sort()
print(len(cntList))
for cnt in cntList:
    print(cnt)