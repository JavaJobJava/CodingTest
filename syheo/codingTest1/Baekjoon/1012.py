#solved.ac
#실버2
#DFS
#유기농 배추
#1012
import sys
input = sys.stdin.readline

#재귀 횟수 제한 
sys.setrecursionlimit(10**9)

def dfs(row,col,visited,graph,M,N):
    yes = 0
    #이동할 수 있는지 검사 
    if row <0 or row>=N or col <0 or col>=M:
        return yes
    if visited[row][col] or graph[row][col]==0:
        return yes 
    visited[row][col]=True
    yes += 1
    #상하좌우 
    yes+=dfs(row-1,col,visited,graph,M,N)
    yes+=dfs(row+1,col,visited,graph,M,N)
    yes+=dfs(row,col-1,visited,graph,M,N)
    yes+=dfs(row,col+1,visited,graph,M,N)

    return yes 
 
#입력 
T = int(input())
sumList = []
for t in range(T):
    sum = 0 
    #가로 세로 배추 수
    M,N,K = map(int,input().split())
    bList = [[0]*M for _ in range(N)]
    kList = []
    #배추 입력 받기 
    for i in range(K):
        a,b = map(int,input().split())
        bList[b][a] = 1 
        kList.append((b,a))
    #DFS 
    visited = [[False]*M for _ in range(N)]

    for _ in kList:
        if dfs(_[0],_[1],visited,bList,M,N):
            sum +=1
    sumList.append(sum)

for _ in sumList:
    print(_)
