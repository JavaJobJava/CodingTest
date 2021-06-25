#CH12 구현 기출
#예제 12-13
#치킨배달
#백준 15686
#골드 5

from collections import deque

def distance(a,b,c,d):
    return abs(a-c)+abs(b-d)

def bfs(a,chickenCnt,M):
    rstList = []
    q = deque([(a,1,[a])])
    while q:
        cur,cnt,chickenList = q.popleft()
        if cnt == M:
            rst = 0
            for house in houses:
                minDis = 101
                for item in chickenList:
                    minDis = min(distance(house[0],house[1],chickens[item][0],chickens[item][1]),minDis)
                rst+=minDis
            rstList.append(rst)

        for i in range(1,chickenCnt):
            pos = cur +i
            if pos<chickenCnt:
                q.append((pos,cnt+1,chickenList+[pos]))
            else:
                break
    return min(rstList)

N,M = map(int,input().split())

maps = []

for i in range(N):
    maps.append(list(map(int,input().split())))

chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if maps[i][j]==2:
            chickens.append((i,j))
        if maps[i][j]==1:
            houses.append((i,j))



answer = int(1e9)

for i in range(0,len(chickens)-M+1):
    answer=min(bfs(i,len(chickens),M),answer)

print(answer)




