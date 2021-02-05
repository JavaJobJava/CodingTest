#CH4 구현
#예제 4-4
#게임 개발 

# N*M 맵 -> 육지or바다 

#방문한 칸의 수 
cnt = 0 

N,M = map(int,input().split())
#방문한 칸 리스트 
visit = [[0] * M for i in range(N)]

#위치 값 (a,b) 보는 방향 dirc 
a,b,dirc = map(int,input().split())
#게임 지도 입력 
gameMap = []
for i in range(N):
    gameMap.append(list(map(int,input().split())))

dx = [-1,0,1,0] #(row 움직임) 북-> 동 -> 남 -> 서 
dy = [0,1,0,-1] #(col 움직임) 북-> 동 -> 남 -> 서 

#dir가 캐릭터가 바라보는 최초 방향 
dir = dirc
while True:
    #flag는 4방향 볼 때 이동했는지 여부 
    flag = 0
    #index는 dx,dy의 index 
    index = dir
    for i in range(4):
        #왼쪽으로 회전 
        index = (index+3)%4
        #이동될 위치 
        da = a+dx[index]
        db = b+dy[index]
        #이동될 위치의 바다 여부, 방문 여부 검사 
        if (visit[da][db]!=1) and (gameMap[da][db]!=1):
            #캐릭터 이동 
            a = da
            b = db
            #방문 위치 표시 
            visit[da][db]=1
            #현재 바라보는 방향 설정 
            dir = index
            flag = 1
            break
    if flag == 0:
        #반대 방향 index 설정 
        index = (dir+2)%4
        da = a+dx[index]
        db = b+dy[index]
        #이동될 위치 바다 검사
        if (gameMap[da][db]!=1):
            a = da
            b = db
            visit[da][db]=1
        else:
            break

#방문한 칸의 수 
for i in visit:
    for j in i:
        if j==1:
            cnt+=1

print(cnt,end="")
