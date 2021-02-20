N = int(input())
pair = int(input())

arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)


count = 0

for i in range(pair):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1



def DFS(v, visited):
    global count

    visited[v] = 1

    for i in range(1,N+1):
        if arr[v][i]==1 and visited[i] == 0 : #연결되어 있고, 방문안했으면
            count += 1
            DFS(i, visited)


DFS(1, visited)

print(count)