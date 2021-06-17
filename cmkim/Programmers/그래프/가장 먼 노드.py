from collections import deque


def solution(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    arr = [[] for _ in range(n + 1)]

    for x, y in edge:
        arr[x].append(y)
        arr[y].append(x)

    bfs(1, visited, arr)

    max_v = max(visited)

    for value in visited:
        if value == max_v:
            answer += 1

    return answer


def bfs(v, visited, arr):
    count = 0
    q = deque([[v, count]]) # 왜 이렇게 해야 되는지? deque 넣을 때 () 와 [] 차이?

    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in arr[v]:
                q.append([e, count])
