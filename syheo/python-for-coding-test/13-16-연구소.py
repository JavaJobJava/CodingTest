#CH13 BFSDFS기출
#예제 13-16
#연구소
#백준 14502
#골드 5

import itertools
from collections import deque

N , M = map(int,input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
maps = []
virus = []
empties = []
wall = 0
whole_visited = [[False]*M for _ in range(N)]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(M):
        if tmp[j]==2:
            virus.append((i,j))
        elif tmp[j]==0:
            empties.append((i,j))
    maps.append(tmp)

wall = N*M-len(virus)-len(empties)

def bfs():

    visited = [[False]*M for _ in range(N)]
    q = deque([])
    #바이러스 모두 출발 시키기 
    for i in range(len(virus)):
        a,b = virus[i]
        q.append((a,b))
        visited[a][b] = True
        whole_visited[a][b] = True
    while q: 
        v = q.popleft()
        for i in range(4):
            r = v[0]+dx[i]
            c = v[1]+dy[i]
            if 0<=r<N and 0<=c<M and not visited[r][c] and maps[r][c]!=1:
                q.append((r,c))
                visited[r][c]=True
                whole_visited[r][c] = True

answer = 0

cases = itertools.permutations(empties,3)

for case in cases:
    for a,b in case:
        maps[a][b]=1
    whole_visited = [[False]*M for _ in range(N)]
    cnt = 0

    bfs()

    #빈 공간 구하기 
    for i in range(N):
        for j in range(M):
            if not whole_visited[i][j]:
                cnt+=1
                
    answer = max(cnt-wall-3,answer)

    for a,b in case:
        maps[a][b]=0

print(answer)