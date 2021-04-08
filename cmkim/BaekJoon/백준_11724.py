n, m = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)
result = 0

def dfs(num):
    visited[num] = 1
    
    for i in range(1, n+1):
        if visited[i] == 0 and arr[num][i] == 1:
            visited[i] = 1
            dfs(i)
    return True



for i in range(m):          #연결리스트
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(i)
        result += 1
print(result)

