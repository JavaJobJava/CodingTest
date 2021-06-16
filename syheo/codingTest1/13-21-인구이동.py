#CH13 BFSDFS기출
#예제 13-21
#인구 이동
#백준 16234
#골드 5

#Pypy3로 통과

#아이디어 : dfs를 통해 한 칸 기준 연합할 수 있는 묶음을 구함.

import sys
sys.setrecursionlimit(10**9)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

#dfs 
def check(row,col,N,L,R):
    for i in range(4):
        r = row+dx[i]
        c = col+dy[i]
        #연합 가능 조건 
        if 0<=r<N and 0<=c<N and not visited[r][c] and L<=abs(maps[r][c]-maps[row][col])<=R:
            visited[r][c]=True
            result.append((r,c))
            check(r,c,N,L,R)


N,L,R = map(int,input().split())

maps = []

for i in range(N):
    maps.append(list(map(int,input().split())))

whole_cnt = 0

while True:
    locations = []
    visited = [[False]*N for _ in range(N)]
    #모든 칸에 대해 반복 
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result = [(i,j)]
                visited[i][j]=True
                check(i,j,N,L,R)
                #연합된 경우가 있으면
                if len(result)>1:
                    locations.append(result)
    #연합 그룹이 아예 없는 경우 
    if not locations:
        break
    #인구 이동 
    for location in locations:
        total = sum([maps[i][j] for i,j in location])
        people = total//len(location)
        for loc in location:
            maps[loc[0]][loc[1]]=people
    #카운트 증가
    whole_cnt+=1

print(whole_cnt)

