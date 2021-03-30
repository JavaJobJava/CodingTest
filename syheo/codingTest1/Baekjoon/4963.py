#solved.ac
#실버2
#BFS
#섬의 개수
#4963
from collections import deque
import sys 
input = sys.stdin.readline
cntList = []
while True:
    w,h = map(int,input().split()) #가로 세로 
    if w ==0 and h==0: 
        break
    #맵 생성
    maps=[[0]*(w+2)]
    for i in range(h):
        tmp=[0]+list(map(int,input().split()))+[0]
        maps.append(tmp)
    maps.append([0]*(w+2))
    #BFS
    visited = [[False]*(w+2) for _ in range(h+2)]  
    q = deque([])
    cnt = 0
    for i in range(1,h+2):
        for j in range(1,w+2):
            if not visited[i][j] and maps[i][j]==1:
                q.append((i,j))
                visited[i][j]=True
                while q:
                    v = q.popleft()
                    for x in range(-1,2,1):
                        for y in range(-1,2,1):
                            vr = v[0]+x
                            vc = v[1]+y
                            if not visited[vr][vc] and maps[vr][vc]==1:
                                q.append((vr,vc))
                                visited[vr][vc]=True
                cnt+=1
    cntList.append(cnt)
#출력 
for cnt in cntList:
    print(cnt)




