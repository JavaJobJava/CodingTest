#프로그래머스 
#고득점 Kit
#dfs/bfs
#level3
#네트워크 

from collections import deque

def bfs(node,n,computers,visited):
    rst = 0
    q = deque([node])
    while q:
        v = q.popleft()
        for i in range(n):
            if computers[v][i]==1 and not visited[i]:
                visited[i]=True
                q.append(i)
                rst+=1
    return rst

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if bfs(i,n,computers,visited):
            answer+=1

    return answer