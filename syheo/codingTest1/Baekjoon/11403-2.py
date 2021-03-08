#solved.ac
#실버1
#플로이드 와샬
#경로 찾기
#11403

#DFS로 풀어보기 

import sys 
input = sys.stdin.readline

#N 입력 
N  = int(input())

result = [[0]*N for _ in range(N)]

graph = [[] for _ in range(N)]
#그래프 입력-> 인접 리스트 
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j]==1:
            graph[i].append(j)


def dfs(v,g,visited):
    for i in graph[g]:
        if not visited[i]:
            visited[i] = True
            result[v][i]=1
            dfs(v,i,visited)

for i in range(N):
    visited =[False]*N
    dfs(i,i,visited)

for i in range(N):
    for j in range(N):
        print(result[i][j],end=' ')
    print('')


