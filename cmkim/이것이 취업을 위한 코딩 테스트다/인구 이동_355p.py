from collections import deque

n, l, r = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


#bfs, visited 사용해서 연합의 위치를 큐에 넣어주기
#1. bfs로 일단 먼저 연합끼리 큐에 넣고 (이때 큐에 넣을수 있으면 True, 못 넣으면 False)
#2. 큐에 넣은 연합애들끼리 통일시킨다
#3. 그 다음 또 bfs를 돌릴수 있는지 없는지 판단하기, bfs를 몇번 돌릴 수 있냐를 물어보는 문제

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * n for _ in range(n)]
union = [[-1] * n for _ in range(n)]
count = 0

def bfs(x, y, index): #x, y로 주어진 나라 위치 기준으로 연합국을 찾아 나가는 과정
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]: #bfs 조건
            if l <= abs(arr[x][y]-arr[nx][ny]) <= r: #두 나라 사이의 인구수차이가 조건을 만족할때
                union[nx][ny] = index
                visited[nx][ny] = 1
                bfs(nx, ny, index)
    return


for i in range(n): #모든 나라에 대해서 연합 index를 union배열에 초기화 시켜주기
    for j in range(n):
        if not visited[i][j]:
            #q = deque((i, j, count)) #bfs 돌릴 초기값 설정
            visited[i][j] = 1
            union[i][j] = count      #bfs 시작위치의 연합 index 설정
            bfs(i, j, count)

            count += 1

for i in range(count):











