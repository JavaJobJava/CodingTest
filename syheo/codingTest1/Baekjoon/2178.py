#solved.ac
#실버1
#DFS
#미로 탈출 
#2178

#visited는 리스트이므로 mutable한 속성을 갖음 -> 깊은 복사가 필요
import sys,copy 
input = sys.stdin.readline

N,M = map(int,input().split())

maps = [] 
for i in range(N):
    maps.append(list(map(int,list(input().rstrip()))))

#dfs 
def dfs(maps,v):
    cntList = []
    visited=[[False]*M for _ in range(N)]
    stack  = [(v[0],v[1],v[2],visited)]
    while stack:
        vertex = stack.pop()
        #예외 처리 
        if vertex[0]>=0 and vertex[0]<N and vertex[1]>=0 and vertex[1]<M:
            cnt = vertex[2]
            row = vertex[0]
            col = vertex[1]
            visiting = copy.deepcopy(vertex[3])
            #방문 가능 여부 판별 
            if not visiting[row][col] and maps[row][col]==1:
                if row == N-1 and col == M-1:
                    cntList.append(cnt)
                #방문 처리 
                else:
                    visiting[row][col]=True
                    stack.extend([(row+1,col,cnt+1,visiting),(row-1,col,cnt+1,visiting),(row,col+1,cnt+1,visiting),(row,col-1,cnt+1,visiting)])
    print(min(cntList))
                

dfs(maps,(0,0,1))
