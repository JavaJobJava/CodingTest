#solved.ac
#실버1
#플로이드 와샬
#경로 찾기
#11403

import sys 
input = sys.stdin.readline

#N 입력 
N  = int(input())
INF = int(1e9)
graph = []
#그래프 입력
for i in range(N):
    graph.append(list(map(int,input().split()))) 

for i in range(N):
    for j in range(N):
        if graph[i][j]==0:
            graph[i][j]=INF

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for i in range(N):
    for j in range(N):
        if graph[i][j]<INF:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print('')
