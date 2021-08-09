from collections import deque
def DFS(v, visited):

    visited[v] = 1
    print(v, end = ' ') # end= ' '  -> 다음 출력값 사이의 간격 조정(줄바꿈도 생략가능)

    for i in range(1, n+1):

        if not visited[i] and arr[v][i] == 1:
            DFS(i, visited)

def BFS(v, visited):
    queue = deque([v])
    visited[v] = 1

    while(queue):
        v = queue.popleft()  # 시작 기준이 되는 값을 잡고 시작한다.
        print(v, end=' ')  # end= ' '  -> 다음 출력값 사이의 간격 조정(줄바꿈도 생략가능)
        for i in range(1, n+1):  # 기준값 주변에 있는 방문하지 않은 값들을 전부 탐색한다.
            if not visited[i] and arr[v][i] == 1:
                queue.append(i)
                visited[i] = 1



n, m, v = map(int, input().split())

arr = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1




DFS(v, visited) #사용할 graph, 시작노드, 방문여부
print('')
visited = [0]*(n+1)
BFS(v, visited)
