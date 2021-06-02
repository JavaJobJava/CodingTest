#CH13 BFSDFS기출
#예제 13-17
#경쟁적 전염
#백준 18405
#실버 1

from collections import deque

N , K = map(int,input().split())
maps = [[(0,0)]*(N+1) for i in range(N+1)] #백신 번호, cnt(초)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
virus = []


for i in range(N):
    tmp = list(map(int,input().split()))
    maps[i][0]=(0,0)
    for j in range(N):
        maps[i+1][j+1]=(tmp[j],0)
        if tmp[j]>=1:
            virus.append((i+1,j+1,0)) #virus 좌표, cnt(초)

S,X,Y = map(int,input().split())

def bfs():
    q = deque(virus)
    while q:
        #print(q)
        row,col,cnt = q.popleft()        
        if cnt == S:
            break
        for i in range(4):
            r = row + dx[i]
            c = col + dy[i]
            if 0<r<=N and 0<c<=N: 
                if maps[r][c][0] == 0:
                    maps[r][c]=(maps[row][col][0],cnt+1)
                    q.append((r,c,cnt+1))
                elif maps[r][c][0] > maps[row][col][0] and maps[r][c][1] == maps[row][col][1]:
                    maps[r][c]=(maps[row][col][0],cnt+1)
                    q.append((r,c,cnt+1))

bfs()
print(maps[X][Y][0])

