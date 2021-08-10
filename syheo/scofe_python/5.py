#c는 시선의 시작 지점
#.은 선호콘텐츠
#x는 비선호 콘텐츠



def dfs(i,j):
    location = (-1,-1)
    #방문 했을 시 
    if visited[i][j]:
        pass 
    elif row==i:
        return (i,j)
    else:
        #방문 처리
        visited[i][j] = True  
        #이동 
        if i+1<=row and maps[i+1][j]=='.': #밑으로 
            cntList[i+1][j]+=cntList[i][j]
            location = dfs(i+1,j)
        else:                              #좌우로 
            if j-1>=0 and maps[i][j-1]=='.':
                cntList[i][j-1]+=cntList[i][j]+1
                location= dfs(i,j-1)
            if j+1<=col and maps[i][j+1]=='.':
                cntList[i][j+1]+=cntList[i][j]+1
                location= dfs(i,j+1)
        
    
    return location

#입력 
col, row = map(int,input().split())
INF = int(1e9)

#맵 생성
maps = []
maps.append(['x' for _ in range(col+1)])

for i in range(row):
    maps.append(['x']+list(input()))

#무한 값 설정 
minLength = INF

#dfs 탐색 
for j in range(0,col+1):
    if maps[1][j]=='c':
        result = [0]
        visited = [[False]*(col+1) for _ in range(row+1)] 
        cntList = [[0]*(col+1) for _ in range(row+1)]
        location =  dfs(1,j)  
        # for x in range(row+1):
        #     for y in range(col+1):
        #         print(cntList[x][y],end=' ')
        #     print('\n')
        # print('===========')
        if location[0]!=-1:
            minLength = min(minLength,cntList[location[0]][location[1]])

#결과값 출력 
if minLength ==INF:
    print(-1)
else:
    print(minLength)


        
        

        
