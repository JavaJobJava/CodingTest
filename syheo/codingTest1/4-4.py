#CH4 구현
#예제 4-4
#게임 개발 

# N*M 맵 -> 육지or바다 
cnt = 0 

N,M = map(int,input().split())
visit = [[0] * M for i in range(N)]

a,b,dirc = map(int,input().split())
gameMap = []
for i in range(N):
    gameMap.append(list(map(int,input().split())))

dx = [-1,0,1,0] #(row 움직임) 북-> 동 -> 남 -> 서 
dy = [0,1,0,-1] #(col 움직임) 북-> 동 -> 남 -> 서 


dir = dirc
while True:
    flag = 0
    print("dir=",dir)
    index = dir
    for i in range(4):
        index = (index+3)%4
        print(index)
        da = a+dx[index]
        db = b+dy[index]
        if (visit[da][db]!=1) and (gameMap[da][db]!=1):
            a = da
            b = db
            visit[da][db]=1
            dir = index
            flag = 1
            break
    print("for 끝")
    if flag == 0:
        index = (dir+2)%4
        da = a+dx[index]
        db = b+dy[index]
        print("정보:",da,db,gameMap[da][db])
        if (gameMap[da][db]!=1):
            a = da
            b = db
            visit[da][db]=1
            print("didi")
        else:
            break

for i in visit:
    for j in i:
        if j==1:
            cnt+=1

print(cnt,end="")
