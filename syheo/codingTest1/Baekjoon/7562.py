#solved.ac
#실버2
#dfs/bfs
#나이트의 이동
#7562
import sys
from collections import deque
input = sys.stdin.readline

#최소이므로 최단경로가 보장되는 ㅋㅋ bfs로 해야되는거임ㅋ
def bfs(cur,dest,visited,moves):
    cnt = 0
    q = deque([(cur,cnt)])
    #bfs 띠딱!
    while q:
        loc,cnt = q.popleft()
        visited[loc[0]][loc[1]]=True
        if loc == dest:
            print(cnt)
            break
        for move in moves:
            row=loc[0]+move[0]
            col=loc[1]+move[1]
            if 0<=row<=x-1 and 0<=col<=x-1:
                if not visited[row][col]:
                    visited[row][col]=True
                    q.append(((row,col),cnt+1))

#이동 경로 
moves=[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)]

for i in range(int(input())):
    #체스판 한변의 길이 
    x = int(input())
    cur = tuple(map(int,input().split()))
    dest = tuple(map(int,input().split()))
    visited = [[False]*(x+1) for _ in range(x+1)]
    bfs(cur,dest,visited,moves)


    




