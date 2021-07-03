"""
@file 네트워크.py
@brief DFS/BFS - Level 3
@desc 
인구이동? 문제랑 비슷(연합국 갯수 구하는 방식) - 하위 문제 같음

"""
from collections import deque


def bfs(visited, computers, start):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        for i in range(len(computers[now])):
            if i != now and computers[now][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)


def solution(n, computers):
    visited = [False] * n
    nNet = 0
    for i in range(n):
        if not visited[i]:
            bfs(visited, computers, i)
            nNet += 1

    return nNet
