#CH5 BFS&DFS
#예제 5-10
# 음료수 얼려 먹기 

# N*M
# 구멍 뚫려 있는 부분 0  , 칸막이가 존재하는 부분은 1
# 구멍 뚫려 있는 부분 끼리 상,하,좌,우로 붙어 있는 경우 서로 연결된걸로 간주
#생성되는 총 아이스크림의 개수를 구하는 프로그램



N,M = map(int,input().split())

graph = [[] for _ in range(N)]
visited = [[False]*M for _ in range(N)]
sum = 0

for i in range(N):
    temp = list(map(int,input()))
    graph[i]=temp

#dfs 
def dfs(row,col):
    cnt=0
    if row<0 or col<0 or row>=N or col>=M:
        pass 
    elif graph[row][col]==1 or visited[row][col]:
        pass
    else:
        #방문 가즈아 
        visited[row][col]=True
        cnt=1
        
        dfs(row-1,col)
        dfs(row,col-1)
        dfs(row+1,col)
        dfs(row,col+1)

    return cnt


for i in range(N):
    for j in range(M):
        sum+=dfs(i,j)

print(sum)



        

