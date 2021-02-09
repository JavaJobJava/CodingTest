#CH5 BFS&DFS
#예제 5-11
#미로 탈출

# N*M에 동빈이가 갇혀 있음
# 동빈이는 (1,1) 미로 출구 (N,M)
# 괴물은 0 
# 움직여야하는 최소 칸의 개수 
# 시작칸과 마지막 칸 세기 

from collections import deque

#입력 
N,M = map(int,input().split())

graph = [ [] for _ in range(N) ]
visited = [ [False]*M for _ in range(N)]
#괴물 몬스터 위치 입력 
for i in range(N):
    graph[i]=list(map(int,input()))

def bfs(row,col):
    cnt = 0 
    #queue 초기화
    queue = deque([(row,col)])
    #현재 위치 방문 
    visited[row][col]=True
    #방문 횟수 추가 
    cnt += 1
    cases=[(0,1),(1,0),(-1,0),(0,-1)]
    while queue:
        #테스트 출력 
        #print(queue)
        #큐에서 제거 
        location = queue.popleft()
        #방문 처리 
        cnt+=1
        #현재 위치 설정 
        row=location[0]
        col=location[1]

        
        
        #상하좌우 이동 
        for case in cases:   
            #다음 위치 
            nextR=row+case[0]
            nextC=col+case[1]
            #이동 가능 여부 예외 처리 
            if nextR <0 or nextC < 0 or nextR>=N or nextC>=M:
                pass
            #괴물이 없다!! or 방문 안했당 
            elif graph[nextR][nextC]!=0 and not visited[nextR][nextC]:
                #경로 누적 값 설정 
                graph[nextR][nextC]+=graph[row][col]
                #방문 가능 노드 추가 
                queue.append((nextR,nextC))
                #방문 설정 
                visited[nextR][nextC]=True
            
    return graph[N-1][M-1]

#최단 경로 길이 
sum = bfs(0,0)
print(sum)

