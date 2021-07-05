from _collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            bfs(n, computers, i, visited)
            answer += 1

    return answer

def bfs(n, computers, i, visited):
    visited[i] = True
    q = deque()
    q.append(i)
    while len(q) > 0:
        now = q.popleft()
        visited[now] = True
        for connect in range(n):
            if connect != now and computers[now][connect] == 1:
                if visited[connect] == False:
                    q.append(connect)